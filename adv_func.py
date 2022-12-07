# def outer():
#     print('i am outer function')
#     def inner():
#         print("i am inner function")
#     inner()
#
# outer()
#
# def welcome(name):
#     print(f'welcome {name}!')
#
# a = welcome
#
# a('ram')
#
# def increment(num):
#     def increase_by(factor):
#         return num + factor
#     return increase_by
#
# increase_by = increment(20)
# print(increase_by(43))
# print(increase_by(67))
#
# def innerWorld(num):
#     def verInnerWorld(factor):
#         return num + factor
#     return  verInnerWorld
#
# increase = innerWorld(12)
# print(increase(56))
#
# #higher order fucntion
# #decorator
#
# def welcome(name):
#     print(f'Welcome {name}')
#
# def bye_bye(name):
#     print(f'Bye bye {name}')
#
# def greet_ram(a):
#     a('ram')
#
# greet_ram(bye_bye)

def decorate_function(example):
    def wrapper():
        print("Called before")
        example()
        print("called after")
    return wrapper

@decorate_function
def example():
    print('hi')

def example2():
    print('hi')

wrapper = decorate_function(example2)
wrapper()

example()


def zero_ho_ki_hoina(func):
    def wrapper(*args,**kwargs):
        if args[1] == 0:
            print("cannot divide by zero")
        else:
            return func(*args,**kwargs)
    return wrapper

@zero_ho_ki_hoina
def division(a,b):
    return a/b

division(4,0)
print(division(4,6))










