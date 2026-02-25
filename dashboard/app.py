import streamlit as st
import pandas as pd
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agents.orchestrator import run_system

st.set_page_config(page_title="Agentic AI Healthcare", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "input"

if "patient" not in st.session_state:
    st.session_state.patient = {}

# ---------------- INPUT PAGE ----------------
def input_page():

    st.title("🧠 Agentic AI Healthcare System")
    st.markdown("### Enter patient vitals to predict health risk")

    age = st.number_input("Age",1,120)
    hr = st.number_input("Heart Rate",30,200)
    spo2 = st.number_input("SpO2",70,100)
    temp = st.number_input("Temperature",34.0,42.0)
    bp = st.number_input("BP",60,200)
    rr = st.number_input("Resp Rate",8,40)
    glucose = st.number_input("Glucose",50,400)
    wbc = st.number_input("WBC",1.0,50.0)
    creatinine = st.number_input("Creatinine",0.1,15.0)

    if st.button("Predict"):

        st.session_state.patient = {
            "age":age,"hr":hr,"spo2":spo2,"temp":temp,
            "bp":bp,"rr":rr,"glucose":glucose,"wbc":wbc,"creatinine":creatinine
        }

        st.session_state.page="output"
        st.rerun()

# ---------------- OUTPUT PAGE ----------------
def output_page():

    data = st.session_state.patient

    st.title("📊 Patient Risk Dashboard")

    result = run_system(
        data["hr"],data["spo2"],data["temp"],
        data["bp"],data["rr"],data["age"],
        data["glucose"],data["wbc"],data["creatinine"]
    )

    st.subheader("Prediction Result")
    st.write(f"Risk Probability: {result['probability']:.2f}")

    if result["risk_level"] == "High":
        st.error("🚨 HIGH RISK PATIENT")
    elif result["risk_level"] == "Moderate":
        st.warning("⚠ MODERATE RISK PATIENT")
    else:
        st.success("✅ LOW RISK PATIENT")

    st.divider()

    st.subheader("Clinical Agent Analysis")
    st.write(result["clinical_desc"])

    st.subheader("Admin Agent Decision")
    st.info(result["guideline"])

    st.subheader("Operational Agent Decision")
    st.warning(result["resource_decision"])

    st.subheader("Final Decision")
    st.success(result["final_decision"])

    if st.button("Check Another"):
        st.session_state.page="input"
        st.rerun()

# ---------------- ROUTER ----------------
if st.session_state.page=="input":
    input_page()
else:
    output_page()
