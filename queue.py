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
    queue.append(task)
    save_queue(queue)


def get_task():
    queue = load_queue()
    if not queue:
        return None

    task = queue.pop(0)
    save_queue(queue)
    return task


import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 queue.py [add <task> | run]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python3 queue.py add <task>")
            sys.exit(1)

        task = sys.argv[2]
        add_task(task)

    elif command == "run":
        from worker import run_worker
        run_worker()

    else:
        print(f"Unknown command: {command}")