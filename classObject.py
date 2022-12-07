
# class Staff:
#
#     #initlizating function
#     def __init__(self,_id,name,contact,designation):
#         self.id=_id
#         self.name = name
#         self.contact = contact
#         self.designation = designation
#
#     def __str__(self):
#         return f"{self.name} - {self.contact}"
#
#     def __repr__(self):
#         return f"{self.name} - {self.contact}"
#
#
#
# staffs = []
#
# for staff in range(0,3):
#     name = input('enter name')
#     _id = staff
#     contact = input('enter contact')
#     designation = input('designation')
#     staffs.append(Staff(_id,name,contact,designation))
#
# for staff in staffs:
#     print('-'*50)
#     print(f'name:{staff.name}')
#     print(f'contact:{staff.contact}')
#     print(f'designation:{staff.designation}')
#     print('-'*50)
#
#
# print(staffs)

class ProductValueError(Exception):
    pass

class Product:

    def __init__(self,name,sku,price):
        self.__name = name
        self.__sku = sku
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def sku(self):
        return self.__sku

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,price):
        if price<=0:
            raise ProductValueError('Price cannot be negative ')
        self.__price = price

    @name.setter
    def name(self,name):
        self.__name = name

    @sku.setter
    def sku(self,sku):
        self.__sku=sku



tshirt = Product('T-shirt','123',500)

tshirt.price=(400)

try:
    tshirt.price=-200
except ProductValueError as err:
    print(err)


tshirt.name=('Tshirt name')
tshirt.sku=('122')

print(tshirt.__dict__)


class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num2+self.num1

    def subtract(self):
        return self.num2-self.num1

    def multiply(self):
        return self.num2*self.num1

    @staticmethod
    def sqaureroot(num):
        return num**0.5


c = Calculator(12,24)
print(c.add())
print(c.subtract())
print(c.multiply())
print(Calculator.sqaureroot(49))
