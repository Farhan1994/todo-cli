def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Deleted task: {task}")
    else:
        print("Task not found.")

