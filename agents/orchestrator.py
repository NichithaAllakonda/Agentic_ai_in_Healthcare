from agents.clinical_agent import predict_risk
from agents.admin_agent import admin_decision
from agents.operations_agent import allocate_resources

def run_system(hr, spo2, temp, bp, rr, age, glucose, wbc, creatinine):

    risk, prob, clinical_desc = predict_risk(hr, spo2, temp, bp, rr, age, glucose, wbc, creatinine)

    guideline = admin_decision(risk)
    resource = allocate_resources(risk)

    final = (
        f"Overall Patient Condition: {risk} Risk.\n"
        f"System recommends appropriate medical and operational response."
    )

    return {
        "risk_level": risk,
        "probability": prob,
        "clinical_desc": clinical_desc,
        "guideline": guideline,
        "resource_decision": resource,
        "final_decision": final
    }
