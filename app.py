def read_tasks(filename):
    with open(filename, "r") as file:
        tasks = file.readlines()
        return [int(t.strip()) for t in tasks]

def calculate_total(tasks):
    return sum(tasks)

def add_overhead(total):
    return total * 1.10

def write_report(filename, total, final):
    with open(filename, "w") as file:
        file.write(f"Total time: {total}\n")
        file.write(f"With overhead: {final}")

tasks = read_tasks("tasks.txt")
total = calculate_total(tasks)
final = add_overhead(total)

write_report("report.txt", total, final)

print("Report created.")