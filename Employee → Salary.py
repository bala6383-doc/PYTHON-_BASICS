salary = { "Emp1": 25000, "Emp2": 30000, "Emp3": 20000 }
max_emp = max(salary, key=salary.get)
print("Highest paid:", max_emp)
