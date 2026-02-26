#!/usr/bin/env python3
"""
Script to calculate position size and risk-to-reward ratio for crypto trades.
"""

import sys
import math
from decimal import Decimal, InvalidOperation


def calculate_position_size_and_risk_reward(total_portfolio_balance, entry_price, stop_loss_price, risk_percentage=1.0, reward_ratio=3.0):
    """
    Calculate position size based on risking a percentage of total portfolio balance
    and compute risk-to-reward ratio.

    Args:
        total_portfolio_balance (float): Total portfolio balance in USD
        entry_price (float): Entry price for the trade in USD
        stop_loss_price (float): Stop loss price for the trade in USD
        risk_percentage (float): Percentage of portfolio to risk (default 1.0 for 1%)
        reward_ratio (float): Standard reward-to-risk ratio (default 3.0 for 3:1)

    Returns:
        dict: Dictionary containing calculated values
    """
    try:
        # Convert inputs to Decimal for precise calculations
        total_portfolio_balance = Decimal(str(total_portfolio_balance))
        entry_price = Decimal(str(entry_price))
        stop_loss_price = Decimal(str(stop_loss_price))
        risk_percentage = Decimal(str(risk_percentage))
        reward_ratio = Decimal(str(reward_ratio))

        # Validate inputs
        if total_portfolio_balance <= 0:
            raise ValueError("Portfolio balance must be greater than zero")

        if entry_price <= 0 or stop_loss_price <= 0:
            raise ValueError("Entry price and stop loss price must be greater than zero")

        if entry_price <= stop_loss_price:
            raise ValueError("Entry price must be greater than stop loss price for a long position")

        if risk_percentage <= 0 or risk_percentage > 100:
            raise ValueError("Risk percentage must be between 0 and 100")

        if reward_ratio <= 0:
            raise ValueError("Reward ratio must be greater than zero")

        # Calculate dollar amount at risk (1% of portfolio)
        dollar_amount_at_risk = (total_portfolio_balance * risk_percentage) / 100

        # Calculate stop loss distance in dollars
        stop_loss_distance = entry_price - stop_loss_price

        # Calculate position size in SOL
        position_size_sol = dollar_amount_at_risk / stop_loss_distance

        # Calculate position value in USD
        position_value_usd = position_size_sol * entry_price

        # Calculate take profit price based on reward ratio
        take_profit_price = entry_price + (stop_loss_distance * reward_ratio)

        # Calculate risk-to-reward ratio
        risk_to_reward_ratio = reward_ratio  # This is the input ratio

        # Calculate potential profit and loss
        potential_profit = position_size_sol * (take_profit_price - entry_price)
        potential_loss = position_size_sol * (entry_price - stop_loss_price)

        # Calculate position percentage of portfolio
        position_percentage_of_portfolio = (position_value_usd / total_portfolio_balance) * 100

        result = {
            "total_portfolio_balance": float(total_portfolio_balance),
            "entry_price": float(entry_price),
            "stop_loss_price": float(stop_loss_price),
            "take_profit_price": float(take_profit_price),
            "position_size_sol": float(position_size_sol),
            "position_value_usd": float(position_value_usd),
            "position_percentage_of_portfolio": float(position_percentage_of_portfolio),
            "dollar_amount_at_risk": float(dollar_amount_at_risk),
            "potential_profit": float(potential_profit),
            "potential_loss": float(potential_loss),
            "risk_percentage": float(risk_percentage),
            "reward_ratio": float(reward_ratio),
            "risk_to_reward_ratio": float(risk_to_reward_ratio)
        }

        return result

    except (ValueError, InvalidOperation) as e:
        print(f"Error: Invalid input - {str(e)}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        return None


def main():
    """
    Main function to handle command line arguments.
    Usage: python calculate_risk.py <portfolio_balance> <entry_price> <stop_loss_price>
    """
    if len(sys.argv) != 4:
        print("Usage: python calculate_risk.py <total_portfolio_balance> <entry_price> <stop_loss_price>")
        print("Example: python calculate_risk.py 10000 25.50 23.00")
        sys.exit(1)

    try:
        total_portfolio_balance = float(sys.argv[1])
        entry_price = float(sys.argv[2])
        stop_loss_price = float(sys.argv[3])

        result = calculate_position_size_and_risk_reward(
            total_portfolio_balance=total_portfolio_balance,
            entry_price=entry_price,
            stop_loss_price=stop_loss_price
        )

        if result:
            print("Risk Management Calculation:")
            print(f"  Portfolio Balance: ${result['total_portfolio_balance']:,.2f}")
            print(f"  Entry Price: ${result['entry_price']:.4f}")
            print(f"  Stop Loss Price: ${result['stop_loss_price']:.4f}")
            print(f"  Take Profit Price: ${result['take_profit_price']:.4f}")
            print(f"  Position Size: {result['position_size_sol']:.6f} SOL")
            print(f"  Position Value: ${result['position_value_usd']:,.2f}")
            print(f"  Position % of Portfolio: {result['position_percentage_of_portfolio']:.2f}%")
            print(f"  Amount at Risk: ${result['dollar_amount_at_risk']:.2f} ({result['risk_percentage']}%)")
            print(f"  Potential Profit: ${result['potential_profit']:.2f}")
            print(f"  Potential Loss: ${result['potential_loss']:.2f}")
            print(f"  Risk-to-Reward Ratio: 1:{result['reward_ratio']}")
        else:
            sys.exit(1)

    except ValueError as e:
        print(f"Invalid input: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()