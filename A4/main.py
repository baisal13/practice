import datetime
import random
import re


class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = UserUtil.generate_email(name, surname, "example.com")
        self.password = UserUtil.generate_password()
        self.birthday = birthday

    def get_details(self):
        return f"ID: {self.user_id}, Name: {self.name} {self.surname}, Email: {self.email}"

    def get_age(self):
        today = datetime.date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))


class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id, None)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            for key, value in user_update.items():
                setattr(cls.users[user_id], key, value)

    @classmethod
    def get_number(cls):
        return len(cls.users)


class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.date.today().year)[-2:]
        random_digits = ''.join(random.choices("0123456789", k=7))
        return int(year_prefix + random_digits)

    @staticmethod
    def generate_password():
        upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        lower = random.choice("abcdefghijklmnopqrstuvwxyz")
        digit = random.choice("0123456789")
        special = random.choice("!@#$%^&*()")
        others = ''.join(
            random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()", k=4))
        password = upper + lower + digit + special + others
        return ''.join(random.sample(password, len(password)))

    @staticmethod
    def is_strong_password(password):
        return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password))

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        return bool(re.match(r"^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$", email))

# Creating a new user
birthday = datetime.date(1995, 6, 15)
user_id = UserUtil.generate_user_id()
new_user = User(user_id, "John", "Doe", birthday)

# Adding user to the service
UserService.add_user(new_user)

# Fetching and displaying user details
retrieved_user = UserService.find_user(user_id)
if retrieved_user:
    print(retrieved_user.get_details())
    print(f"Age: {retrieved_user.get_age()}")

# Checking the number of users
print(f"Total Users: {UserService.get_number()}")

# Updating the user's surname
UserService.update_user(user_id, {"surname": "Smith"})
updated_user = UserService.find_user(user_id)
print(updated_user.get_details())

# Deleting the user
UserService.delete_user(user_id)
print(f"Total Users after deletion: {UserService.get_number()}")
