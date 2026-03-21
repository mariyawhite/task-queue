QUEUE_FILE = "queue.txt"


def load_queue():
    try:
        with open(QUEUE_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


def save_queue(queue):
    with open(QUEUE_FILE, "w") as f:
        for task in queue:
            f.write(task + "\n")


def add_task(task):
    queue = load_queue()

    if task in queue:
        print(f"Task '{task}' already exists. Skipping.")
        return

    queue.append(task)
    save_queue(queue)


def get_task():
    queue = load_queue()
    if not queue:
        return None

    task = queue.pop(0)
    save_queue(queue)
    return task