import yaml
import classes

with open("users.yaml", "rt") as file:
    users = yaml.load(file, Loader=yaml.Loader)

with open("topics.yaml", "rt") as file:
    topics = yaml.load(file, Loader=yaml.Loader)

current_user = ""
focus = ""

## Functions
# updates YAML files
def update_yamls():
    with open("users.yaml", "wt") as file:
        data = yaml.dump(users, sort_keys=False)
        file.write(data)
    with open("topics.yaml", "wt") as file:
        data = yaml.dump(topics, sort_keys=False)
        file.write(data)

def login():
    username = input("""
--------------------------------
Please input your username or (esc)ape.
--------------------------------
""")
    while True:
        try:
            if username in users.keys():
                while True:
                    try:
                        password = input("""
--------------------------------
Please input your password or (esc)ape.
--------------------------------
""")
                        if users[username]["password"] == password:
                            progress = (users[username]["progress"] if "progress" in users[username] else [])
                            print(f"""
--------------------------------
Welcome back, {username}!
--------------------------------
""")
                            current_user = classes.User(username, password, progress)
                            focus = "user_menu"
                            return focus, current_user
                        elif password == "esc":
                            print("Escaping back to menu.\n")
                            focus = input("""
Welcome to the Progress Tracker!
--------------------------------
 -- login
 -- new user
 -- quit
--------------------------------
""")
                            return False
                        else:
                            raise classes.PasswordInvalid
                    except classes.PasswordInvalid:
                        print("Password invalid.\n")

            elif username == "esc":
                print("Escaping back to menu.\n")
                focus = input("""
Welcome to the Progress Tracker!
--------------------------------
 -- login
 -- new user
 -- quit
--------------------------------
""")
                current_user = ""
                return focus, current_user
            else:
                raise classes.UsernameNotFound
        except classes.UsernameNotFound:
            username = input("Username not found.\nPlease input your username or (esc)ape.\n")
        else:
            return False

def create_new_user():
    global focus, current_user
    while True:
        try:
            username = input("Please input a username or (esc)ape.\n")
            if type(username) is None:
                global focus
                focus = input("""
Welcome to the Progress Tracker!
--------------------------------
 -- login
 -- new user
 -- quit
--------------------------------
""")
                current_user = ""
                return focus, current_user
            if username in users.keys():
                raise classes.UsernameAlreadyExists
            elif username == "esc":
                print("Escaping back to menu.\n")
                focus = input("""
Welcome to the Progress Tracker!
--------------------------------
 -- login
 -- new user
 -- quit
--------------------------------
""")
                return focus
            else:
                password = input("Please input a password or (esc)ape.\n")
                if password == "esc":
                    print("Escaping back to menu.\n")
                    focus = input("""
Welcome to the Progress Tracker!
--------------------------------
 -- login
 -- new user
 -- quit
--------------------------------
""")
                    return focus
                progress = []
                current_user = classes.User(username, password, progress)
                users[username] = {
                    "username": username,
                    "password": password,
                    "progress": progress
                }
                update_yamls()
                focus = "user_menu"
                return focus, current_user
                
        except classes.UsernameAlreadyExists:
            print("Username already exists. Try again.")