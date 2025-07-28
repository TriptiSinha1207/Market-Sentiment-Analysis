import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
trader_df = pd.read_csv("historical_data.csv")
sentiment_df = pd.read_csv("fear_greed_index.csv")

# Format dates
trader_df["Date"] = pd.to_datetime(trader_df["Timestamp IST"], format="%d-%m-%Y %H:%M").dt.date
sentiment_df["Date"] = pd.to_datetime(sentiment_df["date"]).dt.date
sentiment_df["Sentiment"] = sentiment_df["classification"].apply(lambda x: "Fear" if "fear" in x.lower() else "Greed")

# Merge datasets
merged_df = pd.merge(trader_df, sentiment_df[["Date", "Sentiment"]], on="Date", how="inner")

# Clean numeric fields
merged_df["Closed PnL"] = pd.to_numeric(merged_df["Closed PnL"], errors="coerce")
merged_df["Size USD"] = pd.to_numeric(merged_df["Size USD"], errors="coerce")

if "Leverage" in merged_df.columns:
    merged_df["Leverage"] = pd.to_numeric(merged_df["Leverage"], errors="coerce").fillna(0)
else:
    merged_df["Leverage"] = 0

# Group by sentiment
sentiment_pnl = merged_df.groupby("Sentiment")["Closed PnL"].agg(["mean", "median", "sum", "count"])
print("Summary of PnL by Sentiment:\n", sentiment_pnl)

# Plot
plt.figure(figsize=(8, 5))
sns.barplot(data=sentiment_pnl.reset_index(), x="Sentiment", y="mean", palette="coolwarm")
plt.title("Average Closed PnL by Market Sentiment")
plt.ylabel("Average Closed PnL")
plt.grid(True)
plt.show()
