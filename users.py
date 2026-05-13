
class User:

    current_date = 
    def __init__(self, first_name, last_name,email, signup_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.signup_date = signup_date


    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def days_since_signup(self, current_date):
        delta = current_date - self.signup_date
        return delta.days
    

user_1 = User('Fahril', 'Ahsan', 'fahril.ahsan@example.com', '2023-01-01')
user_2 = User('Hasna', 'Fikriya', 'hasna.fikriya@example.com', '2023-01-02')


print(user_1.full_name(), user_1.days_since_signup('2023-01-10'))


