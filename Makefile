# Makefile for Solana Trading Agent

install:
	pip install -r requirements.txt

price:
	python skills/sol-price-sentinel/get_sol_price.py

risk:
	python skills/risk-manager/calculate_risk.py 10000 105 100

log:
	python skills/trade-logger/logger.py log buy 20 105

pnl:
	python skills/trade-logger/logger.py pnl
