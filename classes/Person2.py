class Person():
    __name = ''
    __email = ''

    """docstring for Person."""
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self, name):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self, email):
        return self.__email

    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)
# aaron = Person()
# aaron.set_name('Aaron')
# aaron.set_email('aaron@mail.com')
# print(aaron.get_email())

# joe = Person('joe', 'joe@mail.com')
# print(joe.get_name())

# INHERITANCE
class Customer(Person):
    __balance = 0
    """docstring for Customer."""
    def __init__(self, name, email, balance):
        super(Customer, self).__init__(name, email)
        self.__name = name
        self.__email = email
        self.__balance = balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def toString(self):
        return '{} has a balance of {} and can be contacted at {}'.format(self.__name, self.__email)

joe = Customer('Joe Mcmillan', 'joe@mail.com', 50)
joe.set_balance(400)
print(joe.toString())

ryan = Customer('Ryan Ray', 'ryan@mail.com', 400)
print(ryan.toString())
