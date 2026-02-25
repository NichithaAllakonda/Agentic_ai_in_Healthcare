import pandas as pd
import numpy as np
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, confusion_matrix

print("📥 Loading dataset...")

df = pd.read_csv("data/processed/MIMIC-iii.csv")
print("Total rows:", len(df))

# -------- add small noise (important) --------
for col in ["hr","bp","temp","spo2","rr","glucose","wbc","creatinine"]:
    if col in df.columns:
        df[col] = df[col] + np.random.normal(0,2,len(df))

# -------- shuffle --------
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# -------- features --------
features = [
    "age","gender","hr","bp","spo2","temp","rr",
    "glucose","wbc","creatinine","icu_stay_days"
]
features = [f for f in features if f in df.columns]

X = df[features]
y = df["mortality"]

# -------- split --------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# -------- model --------
model = XGBClassifier(
    n_estimators=450,
    max_depth=5,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    gamma=2,
    min_child_weight=5,
    eval_metric="logloss",
    random_state=42
)

print("🧠 Training realistic model...")
model.fit(X_train, y_train)

# -------- predict --------
prob = model.predict_proba(X_test)[:,1]
pred = (prob > 0.5).astype(int)

print("\n🎯 FINAL RESULTS")
print("Accuracy:", accuracy_score(y_test,pred))
print("ROC-AUC:", roc_auc_score(y_test,prob))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test,pred))

print("\nClassification Report:")
print(classification_report(y_test,pred))

joblib.dump(model,"models/xgb_model.pkl")

