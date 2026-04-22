def read_tasks(filename):
    with open(filename, "r") as file:
        tasks = file.readlines()
        return [int(t.strip()) for t in tasks]

def calculate_total(tasks):
    return sum(tasks)

def write_report(filename, total):
    with open(filename, "w") as file:
        file.write(f"Total time with overhead: {total * 1.15}")
tasks = read_tasks("tasks.txt")

total = calculate_total(tasks)

write_report("report.txt", total)

print("Report created.")