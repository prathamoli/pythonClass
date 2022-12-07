class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def profile(self):
        print(f"Username : {self.username}")


class Person(User):
    def __init__(self,username,password,name,address):
        super().__init__(username,password)
        self.name=name
        self.address = address

    def profile(self):
        super().profile()
        print(f"Name : {self.name}")
        print(f"address : {self.address}")


# class Student(Person):
#
#     def __init__(self,name,address,roll_number):
#         super().__init__(name,address)
#         self.roll_number = roll_number
#
#     def profile(self):
#         super().profile()
#         print(f"Roll no : {self.roll_number}")
#
# class Teacher(Person):
#     def __init__(self,name,address,designation):
#         super().__init__(name,address)
#         self.designation = designation

class Staff(Person):
    def __init__(self,username,password,name,address,designation):
        super().__init__(username,password,name,address)
        self.designation = designation

    def profile(self):
        super().profile()
        print(f'Designation : {self.designation}')

staff=Staff('Ram','pasdad','ram','adsjasd','apple')
staff.profile()

