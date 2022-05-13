## Imports and File Loads
import json
import yamlconverter

# load employee dictionary from JSON
with open("employees.json", "r") as employee_load:
    employees = json.load(employee_load)

# load department dictionary from JSON
with open("departments.json", "r") as department_load:
    departments = json.load(department_load)

## Classes
# exceptions
class EntryNotFound(BaseException):
    pass

# employee class (contains function for new employees)
class Employee():
    def __init__(self, first_name, last_name, employ_date, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.employ_date = employ_date
        self.salary = salary
        self.department = department
        self.id = employees["count"]
        employees["count"] += 1

        employees[self.last_name + str(self.id)] = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "employ_date": self.employ_date,
                "salary": self.salary,
                "department": self.department,
            }

        try:
            departments[self.department]["employees"].append(self.last_name + str(self.id))
            print(f'Employee was assigned to the {departments[self.department]["name"]} department')
        except: 
            print("Invalid department id. Employee was not assigned to a department.")

        update_employee_data()
        update_department_data()

        print(f"{self.first_name} was added to the system.\n")

# department class (contains function for new departments)
class Department():
    def __init__(self, name, budget, phone):
        self.name = name
        self.budget = budget
        self.phone = phone
        self.id = departments["count"]
        self.employees = []
        departments["count"] += 1

        departments[self.name + str(self.id)] = {
                "name": self.name,
                "budget": self.budget,
                "phone": self.phone,
                "employees": self.employees
            }

        update_department_data()

        print(f"{self.name} was added to the system.\n")

## Functions
# updates employee JSON file
def update_employee_data():
    with open("employees.json", "w") as employee_dump:
        json.dump(employees, employee_dump)

# updates department JSON file
def update_department_data():
    with open("departments.json", "w") as department_dump:
        json.dump(departments, department_dump)

# creates new employee or department
def create():
    which = input("Create (d)epartment or (e)mployee? (esc)ape is also an option.\n")
    while True:
        try:
            if which == "e":
                first_name = input("Please enter the employee's first name.\n")
                last_name = input("Please enter the employee's last name.\n")
                employ_date = input("Please enter the employee's date of employment.\n")
                salary = input("Please enter the employee's salary.\n")
                department = input("Please enter the employee's department ID if they have one.\n")
                Employee(first_name, last_name, employ_date, salary, department)

            elif which == "d":
                name = input("Please enter the department's name.\n")
                budget = input("Please enter the department's budget.\n")
                phone = input("Please enter the department's phone.\n")
                Department(name, budget, phone)

            elif which == "esc":
                print("Escaping to main menu")
                return False

            else:
                raise Exception
        except:
            which = input("Please choose 'd' or 'e'.\n")
        else: 
            return False

        
# removes employee or department by id
def remove():
    to_remove = input("Please input the id of the employee/department you want to remove. (esc)ape is also an option.\n")
    while True:
        try:
            if to_remove in employees:
                employee_to_remove = to_remove
                for key in employee_list.keys():
                    if key == employee_to_remove:
                        print(f"{key} has been removed.\n")
                        employees.pop(key)
                        employees["count"] -= 1
                        update_employee_data()
                        return
            elif to_remove in departments:
                department_to_remove = to_remove
                for key in department_list.keys():
                    if key == department_to_remove:
                        print(f"{key} has been removed.\n")
                        departments.pop(key)
                        departments["count"] -= 1
                        update_department_data()
                        return
            elif to_remove == "esc":
                print("Escaping to main menu")
                return False
            else:
                raise EntryNotFound
        except EntryNotFound:
            to_remove = input("We couldn't find the entry you were trying to remove. Try again.\n")
        except:
            to_remove = input("Something's wrong. Try again\n")

# updates employee or department information
def update():
    to_update = input("Please enter an id to update. (esc)ape is also an option.\n")
    while True:
        try:
            if to_update in employees:
                for key, value in employee_list.items():
                    to_change = input(""" Updating employee. Please enter an attribute to change.
first_name
employ_date
salary
department
""")
                    if to_change == "esc":
                        print("Escaping to main menu")
                        return False
                    new_info = input("Please enter the new info.\n")
                    if new_info == "esc":
                        print("Escaping to main menu")
                        return False
                    if key == to_update:
                        for att in value:
                            if att == to_change:
                                print(f"{att} will be changed to {new_info}.\n")
                                employees[key][att] = new_info
                                update_employee_data()
                                return
            elif to_update in departments:
                for key, value in department_list.items():
                    to_change = input("""Updating department. Please enter an attribute to change.
phone
budget
""")
                    if to_change == "esc":
                        print("Escaping to main menu")
                        return False
                    new_info = input("Please enter the new info.\n")
                    if new_info == "esc":
                        print("Escaping to main menu")
                        return False
                    if key == to_update:
                        for att in value:
                            if att == to_change:
                                print(f"{att} will be changed to {new_info}.\n")
                                departments[key][att] = new_info
                                update_department_data()
                                return
            elif to_update == "esc":
                print("Escaping to main menu")
                return False
            else:
                raise EntryNotFound
        except EntryNotFound:
            to_update = input("That entry wasn't found. Please try again.\n")

# displays individual employee or department information
def display():
    to_display = input("Please input the id of the employee/department you want to see. (esc)ape is also an option.\n")
    while True:
        try:
            if to_display in employees:
                print(f"""
        First Name: {employees[to_display]["first_name"]}
        Last Name: {employees[to_display]["last_name"]}
        Date of employment: {employees[to_display]["employ_date"]}
        Salary: {employees[to_display]["salary"]}
        Department: {employees[to_display]["department"]}
        """)
                return
            elif to_display in departments:
                print(f"""
        Name: {departments[to_display]["name"]}
        Budget: {departments[to_display]["budget"]}
        Phone: {departments[to_display]["phone"]}
        Employees: {departments[to_display]["employees"]}
        """)
                return
            elif to_display == "esc":
                print("Escaping to the main menu.")
                return False
            else: 
                raise EntryNotFound
        except EntryNotFound:
            to_display = input("Entry not found. Please try again.")




## Main Loop
print("Welcome to the Employee Management System!\n")

focus = "the main menu"
while True:
    try:
        print(f"\nYou are currently examining {focus}.\n")

        # main menu
        if focus == "the main menu":
            focus = input("""
    What would you like to take a look at?
    - (dep)artments
    - (emp)loyees
    - (c)reate new
    - (ex)it
    """)

        # exit
        elif focus == "ex":
            print("Goodbye!")
            break
            
        # departments
        elif focus == "dep":
            print("\nid: department name\n")
            department_list = {key:value for key, value in departments.items() if key != "count"}
            for i in department_list:
                print(f'{i}: {department_list[i]["name"]}\n')
            focus = input(f"""
    - (r)emove department
    - (u)pdate department
    - (d)isplay department
    - (ex)it
    """)

        # employees
        elif focus == "emp":
            print("\nid: first: last")
            employee_list = {key:value for key, value in employees.items() if key != "count"}
            for i in employee_list:
                print(f'{i}: {employee_list[i]["first_name"]}: {employee_list[i]["last_name"]}\n')
            focus = input(f"""
    - (r)emove employee
    - (u)pdate employee
    - (d)isplay employee
    - (ex)it
    """)

        # create
        elif focus == "c":
            create()
            focus = "the main menu"

        # remove
        elif focus == "r":
            remove()
            focus = "the main menu"

        # update
        elif focus == "u":
            update()
            focus = "the main menu"

        # display
        elif focus == "d":
            display()
            focus = "the main menu"

        else:
            raise EntryNotFound
    except EntryNotFound:
        focus = input("Please input a valid option.")

    
yamlconverter.update_yamls()
