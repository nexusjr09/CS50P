# CryptoPulse

#### Video Demo: 

#### Description:

CryptoPulse is a command‑line cryptocurrency dashboard built in Python. It provides live price data, historical charts, portfolio tracking, and price alerts. The project was developed as the final project for CS50P.

**Features:**
- **Live Data:** Fetches current prices, 24h change, and volume from the CoinGecko API.
- **Historical Charts:** Plots price trends with optional moving averages using matplotlib.
- **Portfolio Manager:** Add your holdings and see real‑time value, profit/loss, and asset allocation.
- **Price Alerts:** Set target prices and receive desktop notifications when triggered.
- **Trend Prediction:** Simple indicator (moving average crossover) to suggest short‑term direction.
- **Data Export:** Save portfolio summary or historical data to CSV.

**Files:**

- `project.py` – Contains the main loop and all core functions.
- `test_project.py` – Unit tests for the three key functions: `calculate_sma`, `add_to_portfolio`, and `check_alerts`.
- `requirements.txt` – Lists all external libraries needed (requests, matplotlib, pandas, plyer, pytest).
- `portfolio.json` – Automatically created to persist user holdings.

**Design Choices:**

chose CoinCap.io because it provides a free, reliable, and real-time API for cryptocurrency data. It allows easy access to current prices, market caps, and trading volumes of various cryptocurrencies. Its simple JSON response structure makes it straightforward to extract and use the data in Python projects, which is ideal for building a crypto tracker application.

**Challenges:**

- Handling API rate limits (added a short delay between requests).
- Making the moving average crossover reliable (requires at least 50 data points).
- Testing functions that call external APIs – I used mocking with `unittest.mock`.

This project taught me how to integrate multiple libraries, manage user data, and write testable code. I’m proud of the alert system and the clean chart output.