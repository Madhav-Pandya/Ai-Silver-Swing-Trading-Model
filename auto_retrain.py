import os
import shutil
import subprocess
import pandas as pd
from datetime import datetime
from model_utils import evaluate

BASE = r"E:\personal project\ai silver model trading"
MODEL = os.path.join(BASE, "models", "swing_model.pkl")
BACKUP = os.path.join(BASE, "models", "backup")

os.makedirs(BACKUP, exist_ok=True)

print("Starting retrain...")

# Backup old model
if os.path.exists(MODEL):
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    shutil.copy(
        MODEL,
        os.path.join(BACKUP, f"swing_model_{ts}.pkl")
    )
    print("Old model backed up")

# Download + clean
subprocess.run(["python", "download_etf.py"])
subprocess.run(["python", "clean_data.py"])

# Train new
subprocess.run(["python", "train_swing.py"])

# Compare performance
df = pd.read_csv(os.path.join(BASE,"data","silver_swing_clean.csv"))

old_models = sorted(os.listdir(BACKUP))
old_model = os.path.join(BACKUP, old_models[-1])

old_perf = evaluate(old_model, df)
new_perf = evaluate(MODEL, df)

print("Old model equity:", old_perf)
print("New model equity:", new_perf)

if new_perf > old_perf:
    print("New model is BETTER → Keeping it")
else:
    print("Old model is better → Restoring backup")
    shutil.copy(old_model, MODEL)
