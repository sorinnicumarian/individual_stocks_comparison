# 📈 individual_stocks_comparison

This project is a personal tool designed to analyze and monitor individual stocks to evaluate whether they are **undervalued**, **overvalued**, or fairly priced. The goal is to get daily insights — especially at market open — to help decide if any stock on my watchlist might be a good buying opportunity. It also serves as a way for me to understand stock fundamentals more deeply over time.

## 🔍 Why I Built This

I wanted something lightweight and easy to use that gives me daily stock alerts with real-world metrics that actually matter — not just ticker prices. I began with `GOOGLEFINANCE()` in Google Sheets, but the data it provides is too limited. I then tried the Finnhub API using Google Apps Script — a great step — but the lack of support for Node.js or the official SDK led me to build this project using Python and GitHub Actions.

This repo aims to grow into a more automated, flexible tool that helps track key financial indicators from a custom watchlist and make more informed decisions.

---

## 📊 Parameters Used

These are the initial parameters and example data points:

| Column Name        | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Company Name       | -                                                                           |
| Index              | -                                                                           |
| Current Price      | Current trading price of the stock                                          |
| Market Cap         | Total market value of a company’s outstanding shares                        |
| PE Ratio (TTM)     | Price-to-Earnings Ratio — lower is generally better                         |
| P/B Ratio          | Price-to-Book Ratio — lower is generally better                             |
| ROE                | Return on Equity — higher is better                                         |
| Dividend Yield     | Annual dividend as % of share price — higher is better                      |

### 🎯 What’s Considered Good?

| Metric         | Ideal Value          |
|----------------|----------------------|
| PE Ratio       | < 8                  |
| P/B Ratio      | < 1                  |
| ROE            | > 12%                |
| Dividend Yield | > 3.5%               |

### 🧪 Sample Watchlist (Abbreviated)

| Company           | Symbol | Price | PE Ratio | ROE    | Dividend Yield |
|-------------------|--------|-------|----------|--------|----------------|
| Equifax           | EFX    | 220   | 45.41    | 12.64% | 0.74%          |
| Alphabet          | GOOGL  | 157   | 20.31    | 32.91% | 0.55%          |
| Nvidia            | NVDA   | 110   | 37.45    |119.18% | —              |
| Procter & Gamble  | PG     | 167   | 26.58    | —      | #N/A           |
| Tesla             | TSLA   | 250   |122.58    | —      | —              |
| Apple             | AAPL   | 198   | 31.48    | —      | —              |
| Microsoft         | MSFT   | 388   | 31.29    | —      | —              |

---

## 🚧 Version 0.1 — Early Exploration

- Began with Google Sheets and `GOOGLEFINANCE()` → too limited
- Tried Google Apps Script + Finnhub API → good API access, but no Node.js or SDK support
- Pivoted to **Python** + **GitHub Actions** for flexibility and automation
- Now aiming for:
  - Automated daily analysis
  - Full overwrite (load) into Google Sheets
  - Mobile notifications (non-email)

---

## 📜 License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).

> You are free to use, copy, and modify the code for **non-commercial purposes**.  
> Please give credit to the original author. No commercial or resale use is allowed.

---

Feel free to clone the repo and try it on your own watchlist. Contributions, ideas, or improvements are always welcome!
