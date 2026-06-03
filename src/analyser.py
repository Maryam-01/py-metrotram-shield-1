from src.reader import read_log

def filtered_alerts(logs):
    filtered_alerts = []
    for log in logs:
        if "ERROR" in log or "401" in log:
            filtered_alerts.append(log)
    return filtered_alerts


def parse_alert(clean_alert):
    parts = clean_alert.split()
    
    timestamp = " ".join(parts[0:2])
    level = parts[2]
    message = " ".join(parts[3:])

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }




