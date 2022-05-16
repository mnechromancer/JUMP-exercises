## Imports and File Loads
import classes
import functions

current_user = functions.current_user
focus = functions.focus

## Main Loop
active = True

focus = input("""
Welcome to the Progress Tracker!
--------------------------------
-- login
-- new user
-- quit
--------------------------------
""")
while active:
    try:
        # login
        if focus == "login":
            focus, current_user = functions.login()

        elif focus == "new user":
            focus, current_user = functions.create_new_user()

        elif (focus == "user_menu") and current_user:
            print(current_user)
            action = input("""
--------------------------------
 -- stats
 -- update
 -- logout
--------------------------------
""")
            user_menu = True
            while user_menu:
                try: 
                    if action == "stats":
                        stats_menu = True
                        while stats_menu:
                            choice = input("""
--------------------------------
What would you like to view?
--------------------------------
 -- (complete) entries
 -- (in progress) entries
 -- (incomplete) entries
 -- (summary)
 -- (esc)ape   
--------------------------------
""")
                            try:
                                if choice == "complete":
                                    print("--------------------------------")
                                    completed_stats = current_user.display_complete()
                                    if completed_stats:
                                        for i in completed_stats:
                                            print(i[0])
                                            stats_menu = False
                                    else:
                                        print("No complete entries.")
                                        stats_menu = False
                                elif choice == "in progress":
                                    print("--------------------------------")
                                    in_progress_stats = current_user.display_in_progress()
                                    if in_progress_stats:
                                        for i in in_progress_stats:
                                            print(i[0])
                                            stats_menu = False
                                    else:
                                        print("No entries in progress.")
                                        stats_menu = False
                                elif choice == "incomplete":
                                    print("--------------------------------")
                                    incomplete_stats = current_user.display_incomplete()
                                    if incomplete_stats:
                                        for i in incomplete_stats:
                                            print(i[0])
                                            stats_menu = False
                                    else:
                                        print("No incomplete entries.")
                                        stats_menu = False
                                elif choice == "summary":
                                    print("--------------------------------")
                                    current_user.display_total_progress()
                                    
                                elif choice == "esc":
                                    print("--------------------------------")
                                    print("Escaping to user menu.\n")
                                    stats_menu = False
                                    user_menu = False
                                else:
                                    raise classes.CommandNotFound
                            except classes.CommandNotFound:
                                choice = input("Please choose a valid option.\n")
                    elif action == "update":
                        choice = input("""
--------------------------------
 -- (add) entry
 -- (update) entry
 -- (remove) entry
 -- (esc)ape
--------------------------------
""")
                        update_menu = True
                        while update_menu:
                            try:
                                if choice == "add":
                                    current_user.add_entry()
                                    functions.update_yamls()
                                    update_menu = False
                                    user_menu = False
                                elif choice == "remove":
                                    current_user.remove_entry()
                                    functions.update_yamls()
                                    update_menu = False
                                    user_menu = False
                                elif choice == "update":
                                    current_user.update_entry()
                                    functions.update_yamls()
                                    update_menu = False
                                    user_menu = False
                                elif choice == "esc":
                                    print("Escaping back to menu.\n")
                                    update_menu = False
                                    user_menu = False
                                else:
                                    raise classes.CommandNotFound
                            except classes.CommandNotFound:
                                choice = input("Please choose a valid choice.\n")
                    elif action == "logout":
                        print("Logging out")
                        current_user = ""
                        user_menu = False
                        focus = input("""
Welcome to the Progress Tracker!
--------------------------------
-- login
-- new user
-- quit
--------------------------------
""")
                    else: 
                        raise classes.CommandNotFound
                except classes.CommandNotFound:
                    action = input("Please choose a valid command.\n")
                        


        elif focus == "quit":
            print("Goodbye!")
            active = False

        else:
            raise classes.CommandNotFound
    except classes.CommandNotFound:
        focus = input("Please input a valid option.\n")