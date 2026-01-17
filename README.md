# AI Silver Swing Trading Model 🤖📈

## 📌 Project Overview

This project is an AI-based swing trading model for Silver (XAG/USD). It uses machine learning techniques and technical indicators to generate trade signals and evaluate performance through backtesting.

The goal is to build a data-driven trading system that helps identify profitable swing trades while managing risk effectively.

---

## 🚀 Features

* Historical price data processing
* Technical indicator calculation
* Machine Learning model training
* Automated backtesting system
* Performance metrics (win rate, profit, drawdown)
* Model retraining support 🔁
* Prediction-based trade signals

### 📲 Real-time Telegram trade alerts

* Buy/Sell notifications
* Stop-loss & target updates
* Trade execution confirmations

---

## 📩 Telegram Alert System

This project supports automatic Telegram notifications for trade signals.

### 🔔 Notifications include

* Buy / Sell signal
* Entry price
* Stop-loss
* Take-profit
* Timestamp

### ⚙ Setup

#### 1️⃣ Create your alert bot

1. Open Telegram
2. Message **@BotFather**
3. Use `/newbot`
4. Copy your **Bot Token** 🔑

#### 2️⃣ Get your Chat ID (Using @userinfobot)

1. Open **@userinfobot**
2. Send:

   ```
   /start
   ```
3. You will receive:

   * Your **Id** (this is your Chat ID)
   * Username

#### 3️⃣ Activate your alert bot

* Open your newly created bot
* Send any message ("Hi" or "Start")

> ⚠ This step is mandatory or Telegram will not deliver messages

#### 4️⃣ Configure in project

Edit `main.py`:

```python
BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"  # From @userinfobot
```

---

## 📌 Sample Alert

```
📊 Silver Trade Alert
Action: BUY
Price: 24.85
SL: 24.50
Target: 25.40
Time: 14:32 IST
```

---

## 🛠 Tech Stack

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* pandas-ta
* Joblib

---

## 📂 Project Structure

```
ai-silver-swing-model/
│
├── data/
│   ├── silver_swing_clean.csv
│   └── silver_swing.csv
│
├── model/
│   └── trained_model.pkl
│
├── backtest.py
├── auto_retrain.py
├── main.py
└── README.md
```

---

## ⚙ Installation

```bash
git clone https://github.com/USERNAME/ai-silver-swing-model.git
cd ai-silver-swing-model
```

---

## ▶ How to Run

### 🔧 Auto-train model / Compare old model with new model keep the best

```bash
python auto_retrain.py
```

### 🔧 Train model

```bash
python train_swing.py
```

### 📊 Run backtest

```bash
python backtest.py
```

### 🤖 Predict signals / Run project

```bash
python main.py
```

---

## 📊 Strategy Logic

Uses technical indicators such as:

* RSI
* MACD
* Moving Averages
* ATR

AI model predicts:

* Buy
* Sell
* Hold / No Trade

Trades are executed based on:

* Confidence threshold
* Risk-reward ratio
* Stop-loss and take-profit rules

---

## 📈 Sample Output

```
BACKTEST REPORT
----------------
Starting capital: 100000
Ending capital: 125430
Total trades: 38
Wins: 24
Losses: 14
Win rate: 63.15%
```

---

FOR AUTO RETRAIN / AUTO RUN 

Please configure your system to run main.py every day & auto_retrain every week


---

## 🔁 Auto Retraining

* Supports periodic model retraining
* Compares old model vs new model
* Keeps better performing model
* Do every week(sunday)
---

## ⚠ Disclaimer

This project is for educational purposes only.
Trading involves risk.
I am not responsible for any financial losses.

---

## 🙌 Contribution

Pull requests are welcome.
For major changes, please open an issue first.

---

## 📜 License

MIT License

---

## 👤 Author

Madhav Pandya
