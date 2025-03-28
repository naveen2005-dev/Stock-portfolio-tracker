import tkinter as tk

class Portfolio:
    def _init_(self):
        self.stocks = {
            "AAPL": {"quantity": 10, "purchase_price": 150, "current_price": 170},
            "GOOGL": {"quantity": 5, "purchase_price": 2800, "current_price": 2900},
            "TSLA": {"quantity": 8, "purchase_price": 700, "current_price": 750},
        }

portfolio = Portfolio()

# Create a simple Tkinter window for the portfolio
root = tk.Tk()
root.title("Stock Portfolio Tracker")

def display_portfolio():
    portfolio_summary = "Portfolio Summary:\n"
    for symbol, data in portfolio.stocks.items():
        portfolio_summary += f"{symbol}: {data['quantity']} shares\n"
        portfolio_summary += f"  Purchase Price: ${data['purchase_price']}\n"
        portfolio_summary += f"  Current Price: ${data['current_price']}\n"
        portfolio_summary += "-" * 30 + "\n"
    label.config(text=portfolio_summary)

label = tk.Label(root, text="Welcome to the Stock Portfolio Tracker!", justify=tk.LEFT)
label.pack()

button = tk.Button(root, text="Display Portfolio", command=display_portfolio)
button.pack()

root.mainloop()
 task2
