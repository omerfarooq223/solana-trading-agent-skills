# Risk Manager Skill

## Overview
The Risk Manager skill automates the calculation of position sizing and risk-to-reward ratios for your SOL trades. It addresses the time-consuming task of manually calculating position sizes based on your portfolio balance and risk management principles.

## Components
- `calculate_risk.py`: Python script that calculates position size and risk-to-reward ratio

## Usage
When planning a new SOL trade, Claude should execute the calculate_risk.py script with three inputs:
```
python calculate_risk.py <total_portfolio_balance> <entry_price> <stop_loss_price>
```

For example:
```
python calculate_risk.py 10000 25.50 23.00
```

This will calculate:
- Position size based on risking exactly 1% of the total portfolio balance
- Risk-to-reward ratio assuming a standard 3:1 take-profit target
- Additional risk management metrics

## How Claude Should Use This Skill
1. When the user is planning a new SOL trade, extract the required inputs:
   - Total portfolio balance (in USD)
   - Entry price for SOL (in USD)
   - Stop loss price for SOL (in USD)
2. Execute the calculate_risk.py script with these three values
3. Interpret the results for the user, highlighting:
   - The recommended position size in SOL
   - The position value as a percentage of the total portfolio
   - The risk-to-reward ratio
   - Potential profit and loss amounts

## Output Information
The script provides the following calculations:
- Recommended position size in SOL
- Dollar value of the position
- Position size as a percentage of total portfolio
- Dollar amount at risk (1% of portfolio)
- Take profit price based on 3:1 reward ratio
- Potential profit and loss amounts
- Risk-to-reward ratio

## Risk Parameters
- The script defaults to risking 1% of the total portfolio balance
- The script assumes a 3:1 reward-to-risk ratio for take-profit targets
- These parameters can be modified in the script if different risk management strategies are needed

## Error Handling
The script includes error handling for:
- Invalid numeric inputs
- Negative or zero values for portfolio balance or prices
- Entry price lower than or equal to stop loss price (invalid for long positions)
- Incorrect number of command-line arguments

If the script encounters an error, Claude should verify the input values and ensure they follow the correct format.

## Dependencies
The script uses only built-in Python libraries (sys, math, decimal) and does not require any external dependencies.