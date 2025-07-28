 📊 Market Sentiment vs Trader Performance

This project explores the relationship between Bitcoin market sentiment(Fear vs Greed) and trader performance, using historical trade data from Hyperliquid and sentiment classification from the Bitcoin Fear & Greed Index. The goal is to uncover behavioral patterns that can drive smarter trading strategies.

---

📁 Datasets Used

1. 🧠 Fear & Greed Index

Source: [Alternative.me Index](https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing)
Columns: `date`, `value`, `classification`, `timestamp`
 2. 📈 Hyperliquid Historical Trader Data

Source: [Hyperliquid CSV](https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing)
Columns Include: `Account`, `Execution Price`, `Side`, `Closed PnL`, `Size USD`, `Leverage`, `Timestamp IST`, etc.

🔍 Project Objectives

* Analyze trader profitability during Fear vs Greed periods.
* Identify if sentiment influences trade volume, leverage, and outcomes.
* Provide data-driven insights for designing sentiment-aware trading strategies.

---

 ⚙️ How to Run

 ✅ Requirements

* Python 3.8+
* Jupyter Notebook / Google Colab
* Libraries:

  ```bash
  pip install pandas matplotlib seaborn
  ```

 ▶️ Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/market-sentiment-trader-analysis.git
   cd market-sentiment-trader-analysis
   ```

2. Download the datasets and place them in the root folder:

   * `historical_data.csv`
   * `fear_greed_index.csv`

3. Launch the notebook:

   ```bash
   jupyter notebook Market_Sentiment_Trader_Analysis.ipynb
   ```

---

📊 Visuals Included

* Average Closed PnL by Market Sentiment (Bar Plot)
* Summary statistics: mean, median, total PnL per sentiment class

---
 📌 Key Findings (Sample)

> These will vary based on the dataset, but may include:

* Trades executed during Greed periods have higher PnL on average but also greater volatility.
* Fear periods see lower leverage and lower trade counts.
* Conservative strategies may perform better in high-Fear markets.

---
📁 Project Structure

```
├── Market_Sentiment_Trader_Analysis.py  # Main analysis notebook
├── historical_data.csv                     # Trader data (user provided)
├── fear_greed_index.csv                    # Sentiment index (user provided)
└── README.md                               # This file
```

---

 🧠 Future Enhancements

* Integrate live Fear-Greed API for real-time strategy simulation.
* Add classification model to predict profitable trades using sentiment.
* Segment traders into behavior-based clusters.

---
🤝 Contributing

Feel free to fork the repo and submit a PR with improvements!

---

