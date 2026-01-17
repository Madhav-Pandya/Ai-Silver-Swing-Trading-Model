AI Silver Swing Trading Model
📌 Project Overview

This project is an AI-based swing trading model for Silver (XAG/USD).
It uses machine learning techniques and technical indicators to predict trade signals and evaluate performance through backtesting.

The goal is to build a data-driven trading system that helps identify profitable swing trades while managing risk effectively.

🚀 Features

Historical price data processing

Technical indicator calculation

Machine Learning model training

Automated backtesting system

Performance metrics (win rate, profit, drawdown)

Model retraining support

Prediction-based trade signals

📲 Real-time Telegram trade alerts

Buy/Sell notifications

Stop-loss & target updates

Trade execution confirmations

📩 Telegram Alert System

This project supports automatic Telegram notifications for trade signals.

Notifications include:

Buy / Sell signal

Entry price

Stop-loss

Take-profit

Timestamp

Setup

Create a Telegram bot

Message @BotFather

Use /newbot

Copy your Bot Token

Get your Chat ID

Message your bot

Use:

https://api.telegram.org/bot<TOKEN>/getUpdates


Configure in project

TELEGRAM_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"


Enable alerts

python predict.py

📌 Sample Alert
📊 Silver Trade Alert
Action: BUY
Price: 24.85
SL: 24.50
Target: 25.40
Time: 14:32 IST

🛠 Tech Stack

Python

Pandas

NumPy

Scikit-learn

XGBoost

pandas-ta

Joblib

📂 Project Structure
ai-silver-swing-model/
│
├── data/
│   ├── silver_swing_clean.csv
│   └── silver_swing.csv
|
├── model/
│   └── trained_model.pkl
│
├── backtest.py
├── train.py
├── predict.py
├── requirements.txt
└── README.md

⚙ Installation
git clone https://github.com/USERNAME/ai-silver-swing-model.git
cd ai-silver-swing-model
pip install -r requirements.txt

▶ How to Run
Train model
python train.py

Run backtest
python backtest.py

Predict signals
python predict.py

📊 Strategy Logic

Uses technical indicators such as:

RSI

MACD

Moving Averages

ATR

AI model predicts:

Buy

Sell

Hold

Trades are executed based on:

Confidence threshold

Risk-reward ratio

Stop-loss and take-profit rules

📈 Sample Output
BACKTEST REPORT
----------------
Starting capital: 100000
Ending capital: 125430
Total trades: 38
Wins: 24
Losses: 14
Win rate: 63.15%

🔁 Auto Retraining

Supports periodic model retraining

Compares:

Old model vs new model

Keeps better performing model

⚠ Disclaimer

This project is for educational purposes only.
Trading involves risk.
I am not responsible for any financial losses.

🙌 Contribution

Pull requests are welcome.
For major changes, please open an issue first.

📜 License

MIT License

👤 Author

Madhav Pandya