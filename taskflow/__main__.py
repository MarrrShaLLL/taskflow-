import json
from pathlib import Path
from .models import Task
from .storage import load_tasks, save_tasks
from .display import show_tasks


def main():
    path = Path(__file__).resolve().parent.parent / "tasks.json"
    try:
        tasks = load_tasks(path)
    except (OSError, UnicodeError, ValueError) as error:
        print("Չհաջողվեց բեռնել տվյալները՝", error)
        return

    while True:
        print("\n1. Ցուցադրել | 2. Ավելացնել | 3. Ավարտել | 0. Ելք")
        choice = input("Ընտրություն՝ ").strip()
        if choice == "0":
            print("Ցտեսություն։")
            break
        if choice == "1":
            show_tasks(tasks)
            continue
        try:
            if choice == "2":
                task = Task(input("Վերնագիր՝ "))
                updated = tasks + [task]
            elif choice == "3":
                number = int(input("Առաջադրանքի համարը՝ "))
                if not 1 <= number <= len(tasks):
                    raise ValueError("Այդ համարով առաջադրանք չկա։")
                updated = [Task.from_dict(task.to_dict()) for task in tasks]
                updated[number - 1].complete()
            else:
                print("Ընտրեք մենյուի գործողություններից մեկը։")
                continue
            save_tasks(updated, path)
        except (ValueError, OSError) as error:
            print("Գործողությունը չկատարվեց՝", error)
        else:
            tasks = updated
            print("Պահպանված է։")


if __name__ == "__main__":
    main()
