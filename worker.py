from queue import add_task, get_task

add_task("task1")
add_task("task1")
add_task("task2")

while True:
    task = get_task()
    if not task:
        break
    print(f"processing {task}")