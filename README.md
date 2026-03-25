# Solana (SOL) Trading Agent Skills

This project implements a suite of 3 custom Agent Skills for Claude Code to automate the repetitive cognitive tasks involved in spot cryptocurrency trading. These skills transform a manual monitoring and calculation workflow into a streamlined, agentic process.

## 🚀 Skills Overview

| Skill Name         | Human Task Replaced                                 | Time Saved      | Quality Improvement                                               |
|-------------------|-----------------------------------------------------|-----------------|------------------------------------------------------------------|
| **SOL Price Sentinel** | Manual price & volume monitoring on exchanges/CoinGecko. | ~10 mins / day  | Eliminates "screen fatigue" and ensures real-time data accuracy. |
| **Risk Manager**      | Manual position sizing and Risk-to-Reward calculations.   | ~5 mins / trade | Eliminates human math errors; enforces 1% risk discipline.       |
| **Trade Logger**      | Manual data entry into spreadsheets or journals.          | ~5 mins / trade | Ensures a clean, automated audit trail in `trades.csv`.          |

---

## 🛠 Skill Details

### 1. SOL Price Sentinel (`skills/sol-price-sentinel`)
* **Outcome:** Provides an instant market briefing.
* **Logic:** A Python script that interfaces with the CoinGecko Public API to fetch the current price and 24h trading volume.
* **Usage:** Ask Claude: *"How is SOL looking today?"* or *"Give me a price update."*

**Example CLI usage:**
```sh
python skills/sol-price-sentinel/get_sol_price.py
```

### 2. Risk Manager (`skills/risk-manager`)
* **Outcome:** Generates a precise trade plan.
* **Logic:** Calculates the maximum position size based on a fixed 1% total portfolio risk rule using entry and stop-loss parameters.
* **Usage:** Ask Claude: *"I have $10,000. Plan a trade with $105 entry and $100 stop loss."*

**Example CLI usage:**
```sh
python skills/risk-manager/calculate_risk.py 10000 105 100
```

### 3. Trade Logger (`skills/trade-logger`)
* **Outcome:** Automates portfolio record-keeping.
* **Logic:** Appends trade details (Type, Amount, Price) to a local `trades.csv` and maintains a running balance.
* **Usage:** Ask Claude: *"I just bought 20 SOL at $105. Log this trade."*

**Example CLI usage:**
```sh
python skills/trade-logger/logger.py log buy 20 105
python skills/trade-logger/logger.py pnl
```

---

## 📂 Project Structure
```text
solana_trading_agent/ 
│── README.md
│── my-work-description.md   # Documentation of the manual workflow
├── requirements.txt             # Python dependencies
├── Makefile                     # Automation commands
├── trades.csv                   # Automated trade database
└── skills/
    ├── sol-price-sentinel/
    │   ├── SKILL.md         # Agent instructions
    │   └── get_sol_price.py # API logic
    ├── risk-manager/
    │   ├── SKILL.md         # Agent instructions
    │   └── calculate_risk.py# Math logic
    └── trade-logger/
        ├── SKILL.md         # Agent instructions
        └── logger.py        # CSV/Data logic
```

---

## 🛠 Troubleshooting

- **Missing dependencies:**
    - If you see `ModuleNotFoundError: No module named 'requests'`, run `pip install -r requirements.txt`.
- **Permission errors:**
    - Ensure you have write access to the project directory for logging trades.
- **API errors:**
    - If CoinGecko API fails, check your internet connection or try again later.
- **CSV file issues:**
    - If `trades.csv` is missing, the logger script will create it automatically.
- **General errors:**
    - Check that you are using Python 3.7 or newer.
    - Review the script usage examples above for correct command-line arguments.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork this repository and create a new branch for your feature or fix.
2. Add clear, descriptive commit messages.
3. Ensure your code follows PEP8 and includes docstrings.
4. Add or update tests if applicable.
5. Open a pull request describing your changes and why they improve the project.

For questions or suggestions, please open an issue.

---

**Author:** Muhammad Umar Farooq