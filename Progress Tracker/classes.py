import yaml

## Exceptions
class UsernameNotFound(Exception):
    pass
class UsernameAlreadyExists(Exception):
    pass
class PasswordInvalid(Exception):
    pass
class CommandNotFound(Exception):
    pass
class StatusNotFound(Exception):
    pass
class EntryNotFound(Exception):
    pass

with open("users.yaml", "rt") as file:
    users = yaml.load(file, Loader=yaml.Loader)

with open("topics.yaml", "rt") as file:
    topics = yaml.load(file, Loader=yaml.Loader)


class User:

    def __init__(self, username, password, progress):
        self.username = username
        self.password = password
        self.progress = progress

    def __str__(self):
        statement = f"""
--------------------------------
Username: {self.username}
--------------------------------
"""
        for i in self.progress:
            statement += f"{i[0]}: {i[1]} \n"
        return statement

    def add_entry(self):
        entries_in_use = [i[0] for i in self.progress] if self.progress else []
        entries_not_in_use = [i for i in topics if i not in entries_in_use]
        print("Choose an entry to add or (esc)ape:\n")
        if entries_not_in_use:
            for i in sorted(entries_not_in_use):
                print(i)
        else:
            print("No entries in the topic list that aren't already in use.")
        entry = input("""
--------------------------------
What would you like to add?
You can add something not in the list above and it will be added there, too.
--------------------------------
""")
        if entry not in topics:
            if entry == "esc":
                print("Returning to user menu.\n")
                return
            topics.append(entry)
        status = input("""What is the status of the entry?
--------------------------------
 -- incomplete
 -- in progress
 -- complete
--------------------------------
""")
        while True:
            try:
                if status in ["incomplete", "in progress", "complete"]:
                    self.progress.append([entry, status])
                    return False
                else:
                    raise StatusNotFound
            except StatusNotFound:
                status = input("Please input a valid status.\n")

    def remove_entry(self):
        entries_in_use = [i[0] for i in self.progress] if self.progress else []
        print("""
--------------------------------
Here are the entries available to remove:
--------------------------------
""")
        while True:
            if not entries_in_use:
                print("There are no entries to remove.\n")
                return False
            try:
                for i in entries_in_use:
                    print(i)
                entry = input("""
--------------------------------
Choose an entry to remove or (esc)ape.
--------------------------------
""")
                if entry in entries_in_use:
                    for i in self.progress:
                        if i[0] == entry:
                            self.progress.remove(i)
                            return False
                elif entry == "esc":
                    print("Returning to user menu.\n")
                    return
                else:
                    raise EntryNotFound
            except EntryNotFound:
                entry = input("Please input an entry on the list.\n")

    def update_entry(self):
        entries_in_use = [i[0] for i in self.progress] if self.progress else []
        print("""
--------------------------------
Here are the entries available to update:
--------------------------------
""")
        while True:
            try:
                for i in entries_in_use: 
                    print(i)
                entry = input("Choose an entry to update or (esc)ape.\n")
                if entry in entries_in_use:
                    for i in self.progress:
                        if i[0] == entry:
                            status = input("Enter the new status or (esc)ape.\n")
                            while True:
                                try:
                                    if status in ["incomplete", "in progress", "complete"]:
                                        print("Status updated to:")
                                        i[1] = status
                                        print(i[1])
                                        return
                                        
                                    elif status == "esc":
                                        print("Returning to user menu.\n")
                                        return
                                    else:
                                        raise StatusNotFound
                                except StatusNotFound:
                                    status = input("Please input a valid status or (esc)ape.\n")

                elif entry == "esc":
                    print("Returning to user menu.\n")
                    return
                else:
                    raise EntryNotFound
            except EntryNotFound:
                entry = input("Please input an entry on the list or (esc)ape.\n")

    def display_incomplete(self):
        incomplete_entries = [i for i in self.progress if i[1] == "incomplete"]
        if incomplete_entries:
            return incomplete_entries
        else:
            return []
    
    def display_in_progress(self):
        in_progress_entries = [i for i in self.progress if i[1] == "in progress"]
        if in_progress_entries:
            return in_progress_entries
        else:
            return []

    def display_complete(self):
        complete_entries = [i for i in self.progress if i[1] == "complete"]
        if complete_entries:
            return complete_entries
        else:
            return []

    def display_total_progress(self):
        if self.progress:
            entries_in_use = [i[0] for i in self.progress]
            percent_complete = (len(self.display_complete())/len(entries_in_use)) * 100
            percent_incomplete = (len(self.display_incomplete())/len(entries_in_use))* 100
            percent_in_progress = (len(self.display_in_progress())/len(entries_in_use)) * 100
            print(f"""
--------------------------------
Percent complete: {str(round(percent_complete, 1))}
Percent in progress: {str(round(percent_in_progress, 1))}
Percent incomplete: {str(round(percent_incomplete, 1))}
--------------------------------
""")   
        else: 
            print("This user has no listed entries.")