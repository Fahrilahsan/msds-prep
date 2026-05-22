
from datetime import datetime

class User:

    def __init__(self, first_name, last_name, signup_date):
        self.first_name = first_name
        self.last_name = last_name
        # self.email = email --digantikan dengan method email di bawah, karena kita ingin email selalu update sesuai dengan nama depan dan belakang yang diubah
        self.signup_date = signup_date

    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.email}')"
    
    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@example.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # @property
    # def days_since_signup(self, current_date=None):
    #     signup = datetime.strptime(self.signup_date, '%Y-%m-%d')
    #     if current_date is None:
    #         current_date = datetime.today()
    #     else:
    #         current_date = datetime.strptime(current_date, '%Y-%m-%d')
    #     return (current_date - signup).days
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"
    
    # def __len__(self, current_date=None): # salah, karena __len__ tidak boleh menerima parameter selain self, jadi kita harus buat method biasa untuk menghitung days_since_signup
    #     signup = datetime.strptime(self.signup_date, '%Y-%m-%d')
    #     if current_date is None:
    #         current_date = datetime.today()
    #     else:
    #         current_date = datetime.strptime(current_date, '%Y-%m-%d')
    #     return (current_date - signup).days

    def __len__(self):
        signup = datetime.strptime(self.signup_date, '%Y-%m-%d')
        return (datetime.today() - signup).days

class PaidUser(User):

    def __init__(self, first_name, last_name, signup_date, subscription_tier, expiry_date=None):
        super().__init__(first_name, last_name, signup_date)
        self.subscription_tier = subscription_tier
        self.expiry_date = expiry_date

    def __repr__(self):
        return f"PaidUser('{self.first_name}', '{self.last_name}', '{self.subscription_tier}')"

    # @staticmethod -- salah, karena kita butuh akses ke self.expiry_date
    # def is_active(expiry_date, current_date=None):
    #     if expiry_date is None:
    #         return True
    #     if expiry_date > current_date:
    #         return True
    #     if expiry_date < current_date:
    #         return False
        
    @property
    def is_active(self):
        if self.expiry_date is None:
            return True
        expiry = datetime.strptime(self.expiry_date, '%Y-%m-%d')
        return expiry > datetime.today()
        
    @classmethod
    def from_string(cls, user_str):
        first_name, last_name, signup_date, subscription_tier, expiry_date = user_str.split('|')
        return cls(first_name, last_name, signup_date, subscription_tier, expiry_date)


user_1 = User('Fahril', 'Ahsan', '2026-05-01')
user_2 = User('Hasna', 'Fikriya', '2026-05-02')

paid_user_1 = PaidUser('Siti', 'Aisyah', '2023-01-03', 'Basic', '2025-01-03')
paid_user_2 = PaidUser('Naruto', 'Uzumaki', '2024-01-03', 'Pro', '2027-01-03')

print(user_1)
print(user_1.full_name, len(user_1))

print(user_2)
print(user_2.full_name, len(user_2))

print(paid_user_1.is_active)  # should be False (expired 2025)
print(paid_user_2.is_active)  # should be True (expires 2027)
print(paid_user_1)

new_user = PaidUser.from_string('Budi|Santoso|2024-01-01|Pro|2027-06-01')
print(new_user)
print(new_user.is_active)