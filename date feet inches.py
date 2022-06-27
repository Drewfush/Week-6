from datetime import datetime
datetime_object = datetime.now()
print(datetime_object)
print('Type :- ', type(datetime_object))


def datefeetinch(a, b, c):
    print('Feet =', a)
    print('Inches =', b)
    print('Time =', c)


a = input("Enter the amount of Feet:")
b = input("Enter the amount of Inches:")

datefeetinch(a, b, datetime_object)

