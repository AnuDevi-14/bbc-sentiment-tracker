# BBC News Sentiment Tracker

An automated Python tool that scrapes BBC News headlines daily and tracks sentiment trends over time.

## What it does
- Scrapes live headlines from BBC News using `requests` and `BeautifulSoup`
- Scores each headline's sentiment (positive/negative/neutral) using `VADER`
- Stores results in a CSV file with timestamps, building up data over time
- Analyzes and visualizes daily average sentiment trends using `pandas` and `matplotlib`
- Runs automatically every day via Windows Task Scheduler

## Tech Stack
Python, BeautifulSoup4, VADER Sentiment, Pandas, Matplotlib

## Files
- `scraper.py` — scrapes headlines and saves sentiment scores to CSV
- `analyze.py` — reads CSV, groups by date, and plots sentiment trend chart

## How to run
1. Install dependencies: `pip install requests beautifulsoup4 pandas vaderSentiment matplotlib`
2. Run scraper: `python scraper.py`
3. Run analysis: `python analyze.py`
