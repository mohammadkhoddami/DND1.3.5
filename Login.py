"""

this is login logic that i created it reads passwords and users in txt files and register class save it in those txt files

"""
class Login:
    def login(self, user, password):
        user_list = []
        passwords_list = []
        with open("users.txt", "r") as users:
            user_Lines = users.readlines()
            for c in user_Lines:
                user_list.append(c.replace("\n", ""))
            for i in user_list:
                if user == i:
                    with open("passwords.txt", "r") as passwords:
                        password_lines = passwords.readlines()
                        for u in password_lines:
                            passwords_list.append(u.replace("\n", ""))
                        for b in passwords_list:
                            if password == b:
                                return True
            else:
                print("invalid user or password")
                return False

    def register(self, user, password):
        with open("users.txt", "a") as users:
            users.write(user + "\n")
        with open("passwords.txt", "a") as pw:
            pw.write(password + "\n")
        return user, password
