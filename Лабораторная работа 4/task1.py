# TODO решите задачу
import json
filename = "input.json"

def task() -> float:
    with open(filename) as f:
        json_data = json.load(f)

    # Сумма произведений
    sum_values = sum([item["score"] * item["weight"] for item in json_data])
    # Округление до 3 знака
    return round(sum_values, 3)

print(task())
