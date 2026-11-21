from tabulate import tabulate


def show_tasks(tasks):
    open_count = sum(not task.done for task in tasks)
    completed_count = sum(task.done for task in tasks)

    if not tasks:
        print("Առաջադրանքներ չկան։")
    else:
        rows = []
        for number, task in enumerate(tasks, start=1):
            status = "Ավարտված" if task.done else "Բաց"
            rows.append([number, task.title, status])
        print(tabulate(rows, headers=["Համար", "Վերնագիր", "Վիճակ"],
                       tablefmt="simple"))

    print(f"Բաց առաջադրանքներ՝ {open_count} | Ավարտված առաջադրանքներ՝ {completed_count}")
