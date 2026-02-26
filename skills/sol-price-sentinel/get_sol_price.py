#!/usr/bin/env python3
"""
Script to fetch current SOL price and 24h volume from CoinGecko's public API.
"""

import sys
import json
from datetime import datetime

# Attempt to import requests, with fallback handling
try:
    import requests
except ImportError:
    print("Error: requests library not found. Please install it using: pip install requests", file=sys.stderr)
    sys.exit(1)


def get_sol_price():
    """
    Fetch current SOL price and 24h volume from CoinGecko API.

    Returns:
        dict: Dictionary containing price, volume, and timestamp information
    """
    try:
        # CoinGecko API endpoint for SOL data
        url = "https://api.coingecko.com/api/v3/coins/solana"

        # Make request to CoinGecko API
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse JSON response
        data = response.json()

        # Extract relevant information
        sol_data = {
            "timestamp": datetime.now().isoformat(),
            "coin_id": data.get("id"),
            "symbol": data.get("symbol"),
            "name": data.get("name"),
            "current_price_usd": data["market_data"]["current_price"].get("usd"),
            "price_change_percentage_24h": data["market_data"]["price_change_percentage_24h"],
            "price_change_percentage_7d": data["market_data"]["price_change_percentage_7d"],
            "total_volume_24h_usd": data["market_data"]["total_volume"].get("usd"),
            "market_cap_usd": data["market_data"]["market_cap"].get("usd"),
            "circulating_supply": data["market_data"]["circulating_supply"],
            "last_updated": data["market_data"]["last_updated"]
        }

        return sol_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinGecko API: {str(e)}", file=sys.stderr)
        return None
    except KeyError as e:
        print(f"Error parsing API response: Missing expected field {str(e)}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        return None


def main():
    """Main function to run the script."""
    sol_data = get_sol_price()

    if sol_data:
        print(json.dumps(sol_data, indent=2))
    else:
        print("Failed to fetch SOL price data", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()