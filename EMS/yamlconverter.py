import yaml
import json

def update_yamls():
    employee_data = []
    with open("employees.json", "rt") as employee_load:
        employees = json.load(employee_load)
    with open("employees.yaml", "wt") as file:
        data = yaml.dump(employees, sort_keys=False)
        file.write(data)

    department_data = []
    with open("departments.json", "r") as department_load:
        departments = json.load(department_load)
    with open("departments.yaml", "wt") as file:
        data = yaml.dump(departments, sort_keys=False)
        file.write(data)