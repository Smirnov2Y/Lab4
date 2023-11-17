# TODO решите задачу
import json
def task() -> float:
    with open("input.json") as f:

        data = json.load(f)
        sum_ = 0
        for dic in data:
            score = dic.get("score")
            weight = dic.get("weight")
            sum_ = sum_ + score * weight
    return round(sum_, 3)
    ...


print(task())
