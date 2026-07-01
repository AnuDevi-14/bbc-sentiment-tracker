import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from datetime import datetime
import os

response = requests.get("https://www.bbc.com/news")
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2", attrs={"data-testid": "card-headline"})
headline_texts = [h.text for h in headlines]

analyzer = SentimentIntensityAnalyzer()

rows = []
today = datetime.now().strftime("%Y-%m-%d %H:%M")

for text in headline_texts:
    score = analyzer.polarity_scores(text)
    rows.append({
        "date": today,
        "headline": text,
        "compound": score["compound"]
    })

df = pd.DataFrame(rows)

filename = r"C:\Users\ADMIN\Desktop\bbc_sentiment.csv"
if os.path.exists(filename):
    existing = pd.read_csv(filename)
    df = pd.concat([existing, df], ignore_index=True)

df.to_csv(filename, index=False)
print(f"Saved {len(rows)} headlines. Total rows in file: {len(df)}")
open(r"C:\Users\ADMIN\Desktop\scraper_log.txt", "a").write(today + " - Saved " + str(len(rows)) + " headlines\n")
