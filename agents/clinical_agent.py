import joblib
import numpy as np

model = joblib.load("models/xgb_model.pkl")

def predict_risk(hr, spo2, temp, bp, rr, age, glucose, wbc, creatinine):

    data = np.array([[age, 1, hr, bp, spo2, temp, rr, glucose, wbc, creatinine, 3]])

    prob = model.predict_proba(data)[0][1]

    # ---- RISK CONDITIONS ----
    if prob > 0.70:
        risk = "High"
        desc = "Patient vitals are critically abnormal indicating high mortality risk."
    elif prob > 0.40:
        risk = "Moderate"
        desc = "Patient vitals show moderate abnormalities. Needs observation."
    else:
        risk = "Low"
        desc = "Patient vitals are mostly normal. Patient stable."

    return risk, prob, desc
