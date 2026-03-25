# SOL Price Sentinel Skill

## Overview
The SOL Price Sentinel skill provides real-time market data for Solana (SOL) cryptocurrency, including current price, 24-hour volume, and other relevant market metrics. This skill automates the daily task of monitoring SOL price movements and volume.

## Components
- `get_sol_price.py`: Python script that fetches SOL market data from CoinGecko's public API

## Usage
When requested to provide a market briefing for SOL, Claude should execute the `get_sol_price.py` script to retrieve current market data.

Before first use, ensure the required dependency is installed:
```
pip install requests
```

The script returns:
- Current SOL price in USD
- 24-hour price change percentage
- 7-day price change percentage
- Total 24-hour trading volume in USD
- Market capitalization
- Circulating supply
- Last updated timestamp

## How Claude Should Use This Skill
1. When the user requests current SOL market data or a market briefing, execute the script
2. Parse the returned JSON data to extract relevant information
3. Format the information in a clear, readable way for the user
4. Highlight significant movements (e.g., price changes >5%)
5. Include the timestamp of when the data was retrieved

## Error Handling
If the API request fails, the script will return an error message. Claude should inform the user that:
- The CoinGecko API may be temporarily unavailable
- Network connectivity issues may be preventing data retrieval
- The user might want to try again later

## Example Output
When executed successfully, the script returns a JSON object with the following structure:
```
{
  "timestamp": "2023-10-27T10:30:00.123456",
  "coin_id": "solana",
  "symbol": "sol",
  "name": "Solana",
  "current_price_usd": 25.45,
  "price_change_percentage_24h": 3.21,
  "price_change_percentage_7d": -1.56,
  "total_volume_24h_usd": 1234567890,
  "market_cap_usd": 9876543210,
  "circulating_supply": 384000000,
  "last_updated": "2023-10-27T10:29:55.000Z"
}
```

Claude should format this data appropriately for the user, focusing on the most relevant information for trading decisions.
## Example Output

```
{
  "timestamp": "2023-10-27T10:30:00.123456",
  "coin_id": "solana",
  "symbol": "sol",
  "name": "Solana",
  "current_price_usd": 25.45,
  "price_change_percentage_24h": 3.21,
  "price_change_percentage_7d": -1.56,
  "total_volume_24h_usd": 1234567890,
  "market_cap_usd": 9876543210,
  "circulating_supply": 384000000,
  "last_updated": "2023-10-27T10:29:55.000Z"
}
```