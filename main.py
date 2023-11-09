class Foydalanuvchi:
    def __init__(self, name, username, login, parol):
        self.name = name
        self.username = username
        self.login = login
        self.parol = parol

    def get_name(self):
        return f"{self.name}"

    def get_useername(self):
        return f"{self.username}"

    def get_login(self):
        return f"{self.login}"

    def get_parol(self):
        return f"{self.parol}"

    def get_fullname(self):
        return f"{self.name} {self.username}"

    def get_full_info(self):
        return f"Ism {self.name}, Familya {self.username}, Login: {self.login}, Parol:  {self.parol}"


foydalanuvchi = Foydalanuvchi(f"Shoxrux", "Xasanov", "xsh@gmial.com", "Shox_123")
print(foydalanuvchi.get_full_info())


class Admin(Foydalanuvchi):
    def __init__(self, name, username, login, parol, key):
        super().__init__(name, username, login, parol)
        self.login = login
        self.parol = parol
        self.key = key

    def ban_user(self):
        return f"User {foydalanuvchi.name} - is blocked"

    def admin_info(self):
        return f"Ism {self.name}, Familya {self.username}, Login: {self.login}  Parol: {self.parol} {self.key}"


admin = Admin("Admin", "Xasanov", "admin@gmail.com", "Admin123", "admin")
print(admin.get_full_info())
print(admin.ban_user())
