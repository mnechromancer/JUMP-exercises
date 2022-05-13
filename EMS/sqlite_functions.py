import sqlite3

def define_structure():
    con = sqlite3.connect("ems_db.db")

    create_department_table = """create table departments (
        id integer primary key autoincrement,
        name text,
        budget integer,
        phone text
    );
    """
    create_employee_table = """create table employees (
        id integer primary key autoincrement,
        first_name text,
        last_name text,
        employ_date text,
        salary integer,
        department_id integer,
        foreign key(department_id) references departments(id)
    );
    """

    try:
        with con:
            con.execute(create_department_table)
    except sqlite3.OperationalError as e:
        print(e)

    try:
        with con:
            con.execute(create_employee_table)
    except sqlite3.OperationalError as e:
        print(e)

    con.close()

def create_employee_entry(first_name, last_name, employ_date, salary, department_id):
    con = sqlite3.connect("ems_db.db")
    emp_atts = (first_name, last_name, employ_date, salary, department_id)

    emp_insert_statement = """insert into employees(first_name, last_name, employ_date, salary, department_id) values(?, ?, ?, ?, ?)"""

    try:
        with con:
            con.execute(emp_insert_statement, emp_atts)
    except sqlite3.OperationalError as e:
        print(e)
    else: print("Employee entry successfully created.")

    con.close()


def read_employee_entry(search_by, key):
    con = sqlite3.connect("ems_db.db")

    select_statement = f"""SELECT *
    FROM employees
    WHERE {search_by} = '{key}';
    """

    try:
        with con:
            for row in con.execute(select_statement):
                if row:
                    print(row)
                else:
                    print("No more matching entries.")
    except sqlite3.OperationalError as e:
        print(e)

    con.close()

def update_employee_entry(update_att, update_to, id):
    con = sqlite3.connect("ems_db.db")

    update_statement = f"""UPDATE employees
    SET {update_att} = '{update_to}'
    WHERE id = '{id}';
    """

    try:
        with con:
            con.execute(update_statement)
    except sqlite3.OperationalError as e:
        print(e)

    con.close()

def delete_employee_entry(id):
    con = sqlite3.connect("ems_db.db")

    delete_statement = f"""DELETE FROM employees
    WHERE id = '{id}';
    """

    try:
        with con:
            con.execute(delete_statement)
    except sqlite3.OperationalError as e:
        print(e)
    else:
        print("Employee successfully deleted.")

def create_department_entry(name, budget, phone):
    con = sqlite3.connect("ems_db.db")

    emp_atts = (name, budget, phone)
    emp_insert_statement = """insert into departments(name, budget, phone) values(?, ?, ?);"""

    try:
        with con:
            con.execute(emp_insert_statement, emp_atts)
    except sqlite3.OperationalError as e:
        print(e)
    else: print("Department entry successfully created.")

    con.close()

def read_department_entry(search_by, key):
    con = sqlite3.connect("ems_db.db")
    select_statement = f"""SELECT *
    FROM departments
    WHERE {search_by} = '{key}';
    """
    try:
        with con:
            for row in con.execute(select_statement):
                print(row)
            print("-----------")
    except sqlite3.OperationalError as e:
        print(e)

    con.close()

def update_department_entry(update_att, update_to, id):
    con = sqlite3.connect("ems_db.db")

    update_statement = f"""UPDATE departments
    SET {update_att} = '{update_to}'
    WHERE id = {id};
    """

    try:
        with con:
            con.execute(update_statement)
    except sqlite3.OperationalError as e:
        print(e)

    con.close()

def delete_department_entry(id):
    con = sqlite3.connect("ems_db.db")

    delete_statement = f"""DELETE FROM departments
    WHERE id = {id};
    """

    try:
        with con:
            con.execute(delete_statement)
    except sqlite3.OperationalError as e:
        print(e)
    else:
        print("Department successfully deleted.")

