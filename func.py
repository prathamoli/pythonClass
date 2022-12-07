def example(*args):
    print(args)

example(1,2,3,4,5)

def example2(**kwargs):
    print(kwargs)

example2(name='pratham',contact='98736244',nickname='ra')

def example3(*args,**kwargs):
    print(args)
    print(kwargs)

example3(1,2,3,name='apple',app='oajf')

def multiple_of_factor(num1,factor=5):
    return (num1*factor)

print(multiple_of_factor(3,20))
print(multiple_of_factor(3))
