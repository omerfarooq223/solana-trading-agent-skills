# Trade Logger Skill

## Overview
The Trade Logger skill automates the process of recording trades and calculating profit/loss. It addresses the manual task of maintaining a trade log and calculating P&L by appending trade data to a CSV file and providing P&L summaries.

## Components
- `logger.py`: Python script that logs trades to CSV and calculates total profit/loss
- `trades.csv`: CSV file that stores trade records (created automatically)

## Usage
### Logging Trades
When the user reports a buy or sell action, Claude should execute the logger script with the appropriate parameters:
```
python logger.py log <action> <amount> <price>
```

For example:
- Buy 1.5 SOL at $25.50: `python logger.py log buy 1.5 25.50`
- Sell 0.8 SOL at $28.75: `python logger.py log sell 0.8 28.75`

### Calculating Profit/Loss
To calculate the total profit/loss of all trades, Claude should execute:
```
python logger.py pnl
```

This will provide a summary including:
- Total number of trades
- Total amount bought and sold
- Total value of buys and sells
- Remaining holdings
- Overall profit/loss

## How Claude Should Use This Skill
1. When the user reports a trade (buy or sell), extract the action, amount, and price
2. Execute the logger script to record the trade in the CSV file
3. When requested, execute the pnl command to provide a profit/loss summary
4. The script automatically timestamps each trade entry

## Error Handling
The script includes error handling for:
- Invalid input values
- Missing required parameters
- File access issues
- Invalid action types (must be 'buy' or 'sell')

If the script encounters an error, Claude should inform the user about the specific issue.

## CSV Structure
The trades.csv file contains the following columns:
- Date: Timestamp when the trade was recorded
- Action: 'buy' or 'sell'
- Amount: Quantity of SOL traded
- Price: Price per SOL in USD
- Total_Value: Total value of the trade (Amount * Price)

## Dependencies
The script uses only built-in Python libraries (csv, os, sys, datetime) and does not require any external dependencies.