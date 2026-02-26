# Solana (SOL) Trading Agent Skills

This project implements a suite of 3 custom Agent Skills for Claude Code to automate the repetitive cognitive tasks involved in spot cryptocurrency trading. These skills transform a manual monitoring and calculation workflow into a streamlined, agentic process.

## 🚀 Skills Overview

| Skill Name | Human Task Replaced | Time Saved | Quality Improvement |
| :--- | :--- | :--- | :--- |
| **SOL Price Sentinel** | Manual price & volume monitoring on exchanges/CoinGecko. | ~10 mins / day | Eliminates "screen fatigue" and ensures real-time data accuracy. |
| **Risk Manager** | Manual position sizing and Risk-to-Reward calculations. | ~5 mins / trade | Eliminates human math errors; enforces 1% risk discipline. |
| **Trade Logger** | Manual data entry into spreadsheets or journals. | ~5 mins / trade | Ensures a clean, automated audit trail in `trades.csv`. |

---

## 🛠 Skill Details

### 1. SOL Price Sentinel (`skills/sol-price-sentinel`)
* **Outcome:** Provides an instant market briefing.
* **Logic:** A Python script that interfaces with the CoinGecko Public API to fetch the current price and 24h trading volume.
* **Usage:** Ask Claude: *"How is SOL looking today?"* or *"Give me a price update."*

### 2. Risk Manager (`skills/risk-manager`)
* **Outcome:** Generates a precise trade plan.
* **Logic:** Calculates the maximum position size based on a fixed 1% total portfolio risk rule using entry and stop-loss parameters.
* **Usage:** Ask Claude: *"I have $10,000. Plan a trade with $105 entry and $100 stop loss."*

### 3. Trade Logger (`skills/trade-logger`)
* **Outcome:** Automates portfolio record-keeping.
* **Logic:** Appends trade details (Type, Amount, Price) to a local `trades.csv` and maintains a running balance.
* **Usage:** Ask Claude: *"I just bought 20 SOL at $105. Log this trade."*

---

## 📂 Project Structure
```text
assignment-5-skills/
├── my-work-description.md   # Documentation of the manual workflow
├── README.md                # Project overview and metrics
├── trades.csv               # Automated trade database
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