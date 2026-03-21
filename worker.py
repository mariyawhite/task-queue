COMPLETED_FILE = "completed.txt"


def load_completed():
    try:
        with open(COMPLETED_FILE, "r") as f:
            return set(line.strip() for line in f.readlines())
    except FileNotFoundError:
        return set()


def save_completed(task):
    with open(COMPLETED_FILE, "a") as f:
        f.write(task + "\n")

from queue import add_task, get_task

completed = load_completed()

while True:
    task = get_task()
    if not task:
        break

    if task in completed:
        print(f"skipping already completed {task}")
        continue

    print(f"processing {task}")
    save_completed(task)