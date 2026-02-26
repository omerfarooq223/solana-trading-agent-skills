#!/usr/bin/env python3
"""
Script to log trades to a CSV file and calculate total profit/loss.
"""

import csv
import os
import sys
from datetime import datetime
from decimal import Decimal, InvalidOperation


def initialize_csv(filename='trades.csv'):
    """
    Initialize the CSV file with headers if it doesn't exist.
    """
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Date', 'Action', 'Amount', 'Price', 'Total_Value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            print(f"Created {filename} with headers")


def log_trade(action, amount, price, total_value=None, filename='trades.csv'):
    """
    Append a trade to the CSV file.

    Args:
        action (str): 'buy' or 'sell'
        amount (float or str): Amount of SOL traded
        price (float or str): Price per SOL
        total_value (float or str, optional): Total value of trade (calculated if not provided)
        filename (str): Path to the CSV file
    """
    try:
        # Convert inputs to Decimal for precise calculations
        amount = Decimal(str(amount))
        price = Decimal(str(price))

        # Calculate total value if not provided
        if total_value is None:
            total_value = amount * price
        else:
            total_value = Decimal(str(total_value))

        # Validate action
        if action.lower() not in ['buy', 'sell']:
            raise ValueError("Action must be 'buy' or 'sell'")

        # Initialize CSV if needed
        initialize_csv(filename)

        # Write trade to CSV
        with open(filename, 'a', newline='') as csvfile:
            fieldnames = ['Date', 'Action', 'Amount', 'Price', 'Total_Value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Get current timestamp
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            writer.writerow({
                'Date': current_time,
                'Action': action.lower(),
                'Amount': float(amount),
                'Price': float(price),
                'Total_Value': float(total_value)
            })

        print(f"Trade logged: {action.upper()} {amount} SOL at ${price}/SOL for ${total_value} total")

    except (ValueError, InvalidOperation) as e:
        print(f"Error: Invalid input - {str(e)}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error logging trade: {str(e)}", file=sys.stderr)
        return False

    return True


def calculate_pnl(filename='trades.csv'):
    """
    Calculate the total profit/loss from all trades in the CSV file.
    For simplicity, this calculates unrealized P&L assuming current price of SOL.
    In a real scenario, you'd need to track average buy price vs current market price.

    Args:
        filename (str): Path to the CSV file

    Returns:
        dict: Dictionary containing P&L information
    """
    if not os.path.exists(filename):
        print(f"Error: {filename} does not exist", file=sys.stderr)
        return None

    try:
        buys = []
        sells = []

        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                action = row['Action'].lower()
                amount = float(row['Amount'])
                price = float(row['Price'])

                if action == 'buy':
                    buys.append({'amount': amount, 'price': price})
                elif action == 'sell':
                    sells.append({'amount': amount, 'price': price})

        # Calculate total spent on buys
        total_buy_value = sum(buy['amount'] * buy['price'] for buy in buys)

        # Calculate total received from sells
        total_sell_value = sum(sell['amount'] * sell['price'] for sell in sells)

        # Calculate P&L
        pnl = total_sell_value - total_buy_value

        # Calculate remaining holdings
        total_bought = sum(buy['amount'] for buy in buys)
        total_sold = sum(sell['amount'] for sell in sells)
        remaining_holdings = total_bought - total_sold

        return {
            'total_buy_value': total_buy_value,
            'total_sell_value': total_sell_value,
            'pnl': pnl,
            'total_bought': total_bought,
            'total_sold': total_sold,
            'remaining_holdings': remaining_holdings,
            'trade_count': len(buys) + len(sells)
        }

    except Exception as e:
        print(f"Error calculating P&L: {str(e)}", file=sys.stderr)
        return None


def main():
    """
    Main function to handle command line arguments.
    Usage:
    - Log a trade: python logger.py log buy 1.5 25.50
    - Calculate P&L: python logger.py pnl
    """
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Log a trade: python logger.py log <action> <amount> <price>")
        print("  Calculate P&L: python logger.py pnl")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == 'log':
        if len(sys.argv) != 5:
            print("Usage: python logger.py log <action> <amount> <price>")
            sys.exit(1)

        action = sys.argv[2]
        amount = sys.argv[3]
        price = sys.argv[4]

        success = log_trade(action, amount, price)
        if not success:
            sys.exit(1)

    elif command == 'pnl':
        pnl_data = calculate_pnl()
        if pnl_data:
            print("Profit/Loss Summary:")
            print(f"  Total trades: {pnl_data['trade_count']}")
            print(f"  Total bought: {pnl_data['total_bought']} SOL (${pnl_data['total_buy_value']:,.2f})")
            print(f"  Total sold: {pnl_data['total_sold']} SOL (${pnl_data['total_sell_value']:,.2f})")
            print(f"  Remaining holdings: {pnl_data['remaining_holdings']} SOL")
            print(f"  P&L: ${pnl_data['pnl']:,.2f}")
        else:
            sys.exit(1)

    else:
        print("Unknown command. Use 'log' to log a trade or 'pnl' to calculate profit/loss.")
        sys.exit(1)


if __name__ == "__main__":
    main()