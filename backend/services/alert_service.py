from datetime import datetime

def generate_alerts(recommendations):
    """
    Generates alert messages based on scheme deadlines and priority.
    """

    alerts = []

    for rec in recommendations:
        for reason in rec["explanation"]:
            if "days left" in reason:
                days_left = int(reason.split()[3])
                if days_left <= 7:
                    alerts.append({
                        "scheme_name": rec["scheme_name"],
                        "alert": "Deadline approaching soon"
                    })
                elif days_left <= 30:
                    alerts.append({
                        "scheme_name": rec["scheme_name"],
                        "alert": "Apply soon to avoid missing deadline"
                    })

    return alerts
