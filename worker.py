COMPLETED_FILE = "completed.txt"


def load_completed():
    try:
        with open(COMPLETED_FILE, "r") as f:
            return set(line.strip() for line in f.readlines())
    except FileNotFoundError:
        return set()


def save_completed(task_id):
    with open(COMPLETED_FILE, "a") as f:
        f.write(task_id + "\n")

def run_worker():
    from queue import get_task

    completed = load_completed()

    while True:
        task = get_task()
        if not task:
            break

        if task["id"] in completed:
            print(f"skipping already completed {task}")
            continue

        if task["type"] == "print":
            print(f"processing {task['message']}")
        save_completed(task["id"])
        completed.add(task["id"])