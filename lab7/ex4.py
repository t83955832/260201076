employees = dict()
for _ in range(5):
    name = input("Enter name:")
    salary = int(input("Enter salary:"))
    employees[name] = salary
best_three_salaries = sorted(employees.values())[-3:]
for name in employees.keys():
    salary = employees[name]
    if salary in best_three_salaries:
        print(sorted(name))
    
