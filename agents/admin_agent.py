def admin_decision(risk):

    if risk == "High":
        return ("🚨 Immediate ICU admission required.\n"
                "Hospital admin must alert emergency doctors and prepare ICU support.")

    elif risk == "Moderate":
        return ("⚠ Patient requires close monitoring.\n"
                "Admin should inform duty doctor and keep emergency support ready.")

    else:
        return ("✅ Patient stable.\n"
                "Routine monitoring and regular checkups suggested.")
