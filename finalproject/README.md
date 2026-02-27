> **CRYPTO SENTINEL: A CLI Market Intelligence Tool**


###Video Demo: 

###DESCRIPTION OF THE TOOL:

Crypto Sentinel is a command-line tool built in Python that helps crypto enthusiasts get a quick, "no-nonsense" report on their favorite coins. Instead of opening a browser and getting lost in complex charts, this tool pulls live data directly into your terminal, calculates your potential profits, and gives you a "Market Mood" based on current price volatility.

###ITS WORKING MECHANISM:

When you run the program, it asks you for a cryptocurrency ticker (like BTC or ETH). It then connects to the CoinGecko API to grab the most recent price and the 24-hour price change. If you choose to, you can also enter the price you originally bought at, and the program will instantly calculate your percentage gain or loss. Finally, it displays everything in a clean, color-coded table.

``FILES INCLUDED: ``

>project.py: This is the heart of the application. It contains the main function and the core logic for fetching data, calculating percentages, and determining the market "vibe."

>test_project.py: This file contains the pytest functions. It ensures that the math behind the profit calculations and the user-input cleaning works perfectly every time.

>requirements.txt: A simple list of the external libraries needed (requests for data and rich for the pretty terminal interface).

README.md: This file, explaining the project.

>Why I Made These Design Choices:
The API: I chose the CoinGecko API because it’s free, doesn't require a complex "API Key" for basic use, and provides reliable data for thousands of coins.

>The Rich Library: Most terminal programs look boring. I used the rich library because it allows for "Live" displays, tables, and colors. This makes the data much easier to read at a glance—showing green for profits and red for losses.

>Modular Functions: I decided to keep the API fetching and the "Market Mood" logic in separate functions. This made it much easier to write tests. For example, I could test the "Market Mood" function with "fake" numbers to make sure it correctly identifies a market crash without actually needing the internet.

>Error Handling: I spent a lot of time making sure the program doesn't crash if a user types a coin that doesn't exist. The program will gently tell the user the ticker is invalid instead of throwing a scary Python error.

>Project Goals:
Good outcome: A working tool that displays the current price of Bitcoin.

Better outcome: A tool that calculates profit/loss and formats everything in a beautiful table.

Best outcome: A tool that analyzes volatility and provides a "Buy/Hold/Sell" recommendation based on logic.