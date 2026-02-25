def allocate_resources(risk):

    if risk == "High":
        return ("🏥 ICU bed allocated.\n"
                "Critical care team alerted and ventilator support prepared.")

    elif risk == "Moderate":
        return ("🛏 Observation ward allocated.\n"
                "Nurse monitoring and doctor review scheduled.")

    else:
        return ("🟢 General ward sufficient.\n"
                "Basic monitoring devices allocated.")
