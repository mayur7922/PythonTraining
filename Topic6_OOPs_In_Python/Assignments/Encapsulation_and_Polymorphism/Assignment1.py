class UserAccount:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password  

    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            print("Password changed successfully.")
        else:
            print("Incorrect old password.")

    def check_password(self, password):
        return self.__password == password

if __name__ == "__main__":
    user = UserAccount("Alice", "initial_password")
    print(user.check_password("initial_password"))
    user.change_password("initial_password", "new_password")
    print(user.check_password("new_password"))
