import json
# TODO решите задачу

filename = "input.json"


def task() -> float:
    with open(filename, 'r', encoding='utf-8') as f:
        p_file = json.load(f)

    result = sum([p["score"] * p["weight"] for p in p_file])
    return round(result, 3)


print(task())
