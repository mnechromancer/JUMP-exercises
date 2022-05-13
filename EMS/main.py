import sqlite_functions as sf

sf.define_structure()

active = True
while active:
    focus = input("""Welcome to the EMS. Select:
-- (E)mployees
-- (D)epartments
-- (Q)uit
""")
    while focus == 'E':
        action = input("""What would you like to do in the employees table?
-- (C)reate employee
-- (R)ead employee
-- (U)pdate employee
-- (D)elete employee
-- (esc)ape
""")
        while action == 'C':
            first_name = input("First name:")
            last_name = input("Last name:")
            employ_date = input("Date of employement:")
            salary = int(input("Salary:"))
            department_id = int(input("Department ID:"))
            sf.create_employee_entry(first_name, last_name, employ_date, salary, department_id)
            action = ''

        while action == 'R':
            search_by = input("Filter by:")
            key = input("Search for:")
            sf.read_employee_entry(search_by, key)
            action = ''

        while action == 'U':
            id = input("Employee ID:")
            update_att = input("What would you like to update?")
            update_to = input("Update to:")
            sf.update_employee_entry(update_att, update_to, id)
            action = ''

        while action == 'D':
            id = input("Employee ID:")
            sf.delete_employee_entry(id)
            action = ''

        while action == 'esc':
            focus = ''
            action = ''

    while focus == "D":
        action = input("""What would you like to do in the departments table?
-- (C)reate department
-- (R)ead department
-- (U)pdate department
-- (D)elete department
-- (esc)ape
""")
        while action == 'C':
            name = input("Department name: ")
            budget = int(input("Budget: "))
            phone = int(input("Phone number: "))
            sf.create_department_entry(name, budget, phone)
            action = ''

        while action == 'R':
            search_by = input("Filter by:")
            key = input("Search for:")
            sf.read_department_entry(search_by, key)
            action = ''

        while action == 'U':
            id = input("Department ID:")
            update_att = input("What would you like to update?")
            update_to = input("Update to:")
            sf.update_department_entry(update_att, update_to, id)
            action = ''

        while action == 'D':
            id = input("Department ID:")
            sf.delete_department_entry(id)
            action = ''

        while action == 'esc':
            focus = ''
            action = ''

    while focus == 'Q':
        active = False
        focus = ''


            