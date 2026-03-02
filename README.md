🧠 Agentic AI-Based Healthcare Decision Support System
📌 Overview

This project presents a Multi-Agent Healthcare Decision Support System designed for ICU mortality risk prediction and hospital operations optimization.

The system integrates Machine Learning (XGBoost) with an Agentic AI architecture to transform structured ICU patient data into coordinated clinical and operational decisions.

Unlike traditional static ML models, this system combines:

🔬 Mortality Risk Prediction

🏥 Clinical Guideline Recommendation

⚙️ ICU Resource Allocation

🧠 Multi-Agent Orchestration

📊 Real-Time Dashboard Visualization


🚀 Key Features

ICU Mortality Risk Prediction using XGBoost

Multi-Agent Modular Architecture

Risk-Based Clinical Protocol Recommendation

Reinforcement Learning-Based ICU Resource Allocation

Fairness & Bias Monitoring

Structured & Explainable Outputs

Real-Time Streamlit Deployment  

🏗️ System Architecture
MIMIC-III Dataset
        ↓
Preprocessing & Feature Engineering
        ↓
XGBoost Mortality Model
        ↓
Streamlit Dashboard Interface
        ↓
Multi-Agent System
   ├── Clinical Agent (Risk Prediction)
   ├── Admin Agent (Guideline Retrieval)
   ├── Operations Agent (Resource Allocation)
   └── Orchestrator (Decision Coordination)
        ↓
Final Risk Intelligence Dashboard

** The architecture ensures: **
Modular separation of responsibilities

Scalable agent coordination

End-to-end explainability

Real-time decision support 

🧠 Agents Description

1️⃣ Clinical Agent
Predicts mortality probability
Computes severity score
Classifies risk as Low / Medium / High

2️⃣ Admin Agent
Maps predicted risk to ICU clinical protocols
Retrieves guideline recommendations

3️⃣ Operations Agent
Simulates ICU resource conditions
Allocates beds and staff using reinforcement learning logic

4️⃣ Orchestrator Agent
Integrates all agent outputs
Produces structured, explainable final decision 

📊 Model Details

Model: XGBoost Classifier
Scaling: StandardScaler
Hyperparameter Tuning: Grid Search
Class Imbalance Handling: scale_pos_weight
Probability Calibration Applied

📈 Performance Metrics

Accuracy: 99.2%
Recall: 1.0 (Zero False Negatives)
F1 Score: 0.99+
ROC-AUC: 1.0 

🏥 Risk Classification Logic

| Probability | Risk Level |
| ----------- | ---------- |
| > 0.75      | HIGH       |
| 0.40–0.75   | MEDIUM     |
| ≤ 0.40      | LOW        |

⚙️ Technologies Used

Python
XGBoost
Scikit-learn
NumPy & Pandas
Streamlit
Gym (Custom Hospital Environment)
Joblib 

📂 Project Structure

├── agents/
│   ├── clinical_agent.py
│   ├── admin_agent.py
│   ├── operations_agent.py
│   ├── ethics_agent.py
│   ├── orchestrator.py
│
├── models/
│   ├── xgb_model.pkl
│   ├── scaler.pkl
│   ├── feature_order.pkl
│
├── dashboard/
│   └── app.py
│
├── train_model.py
├── hospital_env.py
├── preprocess_mimic.py
├── requirements.txt
└── README.md

🔬 Dataset

MIMIC-III ICU dataset
Structured vitals, labs, demographics
Mortality as target variable 

📌 Future Enhancements:

spital dataset validation

SHAP-based model explainability

Real-time EHR integration

Cloud deployment

Wearable sensor data integration

Outputs:
<img width="1920" height="1080" alt="Screenshot (290)" src="https://github.com/user-attachments/assets/e913aa70-083e-4b58-bf29-516ed2fb70d4" /> 

<img width="1920" height="1080" alt="Screenshot (287)" src="https://github.com/user-attachments/assets/12fcb8af-dc09-4885-a85b-6f3192814161" /> 

<img width="1920" height="1080" alt="Screenshot (289)" src="https://github.com/user-attachments/assets/939c6315-04ba-47d8-a1d9-cee0237803a5" /> 

<img width="1920" height="1080" alt="Screenshot (288)" src="https://github.com/user-attachments/assets/76091837-0828-4295-8eed-b5374e301645" /> 





