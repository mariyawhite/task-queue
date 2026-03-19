queue = []

def add_task(task):
    queue.append(task)

def get_task():
    if queue:
        return queue.pop(0)
    return None