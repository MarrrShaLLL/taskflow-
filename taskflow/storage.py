import json
from .models import Task


def save_tasks(tasks, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump([task.to_dict() for task in tasks], file,
                  ensure_ascii=False, indent=2)


def load_tasks(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    if not isinstance(data, list):
        raise ValueError("JSON-ի հիմնական արժեքը պետք է լինի list։")
    return [Task.from_dict(item) for item in data]
