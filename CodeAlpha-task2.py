import os

# 1. Hardcoded Stock Prices Dictionary (Current market prices are hardcoded for simplicity)
STOCK_PRICES = {
    "AAPL": 180.50,  # Apple Inc.
    "GOOGL": 155.25, # Alphabet Inc. (Google)
    "TSLA": 250.75,  # Tesla, Inc.
    "AMZN": 185.00,  # Amazon.com, Inc.
    "MSFT": 420.00,  # Microsoft Corp.
    "V": 270.30     # Visa Inc.
}

def get_user_portfolio():
    """
    Prompts the user to enter stock holdings (symbol and quantity).
    Returns a list of dictionaries representing the user's portfolio.
    """
    portfolio = []
    print("\n--- Enter Your Stock Holdings ---")
    print("Available stocks: " + ", ".join(STOCK_PRICES.keys()))
    print("Enter 'done' when finished.")

    while True:
        symbol = input("Enter Stock Symbol (e.g., AAPL): ").strip().upper()

        if symbol == 'DONE':
            break

        if symbol not in STOCK_PRICES:
            print(f"Error: '{symbol}' is not a recognized stock symbol in our price list. Please try again.")
            continue

        while True:
            try:
                quantity = int(input(f"Enter Quantity for {symbol}: "))
                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")

        portfolio.append({
            'symbol': symbol,
            'quantity': quantity
        })
        print(f"Added {quantity} shares of {symbol} to your portfolio.")

    return portfolio

def calculate_investment_value(portfolio):
    """
    Calculates the total investment value based on the portfolio and hardcoded prices.
    Returns the total value (float) and a list of individual stock values.
    """
    total_value = 0.0
    detailed_values = []

    for item in portfolio:
        symbol = item['symbol']
        quantity = item['quantity']
        price = STOCK_PRICES.get(symbol, 0) # Get price from the dictionary
        
        # Basic arithmetic: Total value = Quantity * Price
        stock_value = quantity * price
        total_value += stock_value

        detailed_values.append({
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'value': stock_value
        })

    return total_value, detailed_values

def save_results(total_value, detailed_values, filename="portfolio_summary.txt"):
    """
    Saves the calculated results to a text file.
    """
    try:
        with open(filename, 'w') as f:
            f.write("--- Stock Portfolio Tracker Summary ---\n")
            f.write(f"Timestamp: {os.path.getctime('.')}\n\n")

            f.write("Individual Stock Values:\n")
            for item in detailed_values:
                f.write(f"  {item['symbol']} | Qty: {item['quantity']} | Price: ${item['price']:.2f} | Value: ${item['value']:.2f}\n")
            
            f.write("-" * 40 + "\n")
            f.write(f"TOTAL INVESTMENT VALUE: ${total_value:,.2f}\n")
            f.write("-" * 40 + "\n")
        
        print(f"\n[File Saved] Results successfully saved to {filename}")
    except IOError:
        print(f"\n[Error] Could not write results to {filename}.")

def main():
    """
    Main function to run the portfolio tracker.
    """
    print("=========================================")
    print("  Simple Dictionary-Based Stock Tracker  ")
    print("=========================================")

    # Get user portfolio
    user_portfolio = get_user_portfolio()

    if not user_portfolio:
        print("\nNo stocks entered. Exiting program.")
        return

    # Calculate values
    total_value, detailed_values = calculate_investment_value(user_portfolio)

    # Display results
    print("\n=========================================")
    print("      PORTFOLIO VALUE CALCULATION      ")
    print("=========================================")
    
    for item in detailed_values:
        print(f"Stock: {item['symbol']:<5} | Quantity: {item['quantity']:<5} | Price: ${item['price']:.2f} | Value: ${item['value']:,.2f}")
    
    print("-----------------------------------------")
    print(f"TOTAL PORTFOLIO VALUE: ${total_value:,.2f}")
    print("-----------------------------------------")

    # Optional: Save results
    save_option = input("\nDo you want to save the summary to a file? (y/n): ").strip().lower()
    if save_option == 'y':
        save_results(total_value, detailed_values)
    else:
        print("Results not saved. Have a nice day!")

if __name__ == "__main__":
    main()
