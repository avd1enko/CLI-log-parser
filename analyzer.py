import json
def error_analyzer(data: dict):
    if data.get("status","0").startswith("4") or data.get("status", "0").startswith("5"):
        return json.dumps(data, indent=4)
    return "Ошибок нет"

