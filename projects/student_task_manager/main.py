print("Student Task Manager")
print("--------------------")

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

add_task("Complete Git practical")

print("\nCurrent Tasks:")
for task in tasks:
    print("-", task)
