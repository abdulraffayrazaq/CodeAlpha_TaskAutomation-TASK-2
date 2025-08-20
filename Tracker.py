import random

def portfolio_tracker():
    # Stock list (symbol: price)
    stocks = {
        "AAPL": 180.50, "MSFT": 325.40, "GOOG": 135.20,
        "TSLA": 250.75, "AMZN": 150.30, "NVDA": 450.60, "META": 310.25
    }

    line = "─" * 46
    print("┌" + line + "┐")
    print("│        📊  STOCK PORTFOLIO TRACKER        │")
    print("└" + line + "┘")

    # Show available stocks first
    print("\nAvailable Stocks (symbol → price):")
    for s in sorted(stocks):
        print(f" • {s:<5} → ${stocks[s]:.2f}")

    portfolio = {}

    while True:
        # Fun random suggestion
        tip = random.choice(list(stocks.keys()))
        print("\n💡 Suggestion: consider", tip)
        print("Type a symbol from the list, or 'done' to finish.")

        stock = input("👉 Stock: ").strip().upper()
        if stock == "DONE":
            break
        if stock not in stocks:
            print("❌ Not available. Pick a symbol shown above.")
            continue

        qty_str = input(f"🧮 Shares of {stock}: ").strip()
        if not qty_str.isdigit() or int(qty_str) <= 0:
            print("❌ Please enter a positive whole number.")
            continue

        qty = int(qty_str)
        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"✅ Added {qty} share(s) of {stock}")

    if not portfolio:
        print("\nNo stocks entered. Goodbye!")
        return

    # Summary
    print("\n" + "═" * 48)
    print("            📈  PORTFOLIO SUMMARY")
    print("═" * 48)
    print(f"{'SYMBOL':<8}{'QTY':>6}{'PRICE':>12}{'VALUE':>16}")
    print("─" * 48)

    total = 0.0
    for s in sorted(portfolio):
        q = portfolio[s]
        p = stocks[s]
        v = q * p
        total += v
        print(f"{s:<8}{q:>6}{p:>12.2f}{v:>16.2f}")

    print("─" * 48)
    print(f"{'TOTAL VALUE':<26}${total:>21.2f}")
    print("═" * 48)
    print("✅ Tip: Add more symbols next time to expand your portfolio!\n")

# Run
portfolio_tracker()
