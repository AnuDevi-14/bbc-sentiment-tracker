import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ADMIN\Desktop\bbc_sentiment.csv")

df['date_only'] = pd.to_datetime(df['date']).dt.date

daily_avg = df.groupby('date_only')['compound'].mean()

print(daily_avg)

plt.figure(figsize=(8, 5))
plt.plot(daily_avg.index, daily_avg.values, marker='o')
plt.title("Average BBC News Sentiment by Day")
plt.xlabel("Date")
plt.ylabel("Average Sentiment (Compound Score)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()