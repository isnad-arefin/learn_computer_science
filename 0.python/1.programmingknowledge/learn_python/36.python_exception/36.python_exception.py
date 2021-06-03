# result = None
# a = float (input('Number 1: '))
# b = float (input('Number 2: '))
#
# try:
#     result = a/b
# except:
#     print("float division by zero")
#
# print('Result =', result)
# print('End')



# result = None
# a = float (input('Number 1: '))
# b = float (input('Number 2: '))
#
# try:
#     result = a/b
# except Exception as e:
#     print("Error = ", type(e))
#
# print('Result =', result)
# print('End')



# result = None
# a = (input('Number 1: '))
# b = float (input('Number 2: '))
#
# try:
#     result = a / b
# except ZeroDivisionError as e:
#     print("Error = ", type(e))
#
# print('Result = ', result)
# print('End')



result = None
a = float (input('Number 1: '))
b = float (input('Number 2: '))

try:
    result = a / b
except ZeroDivisionError as e:
    print("ZeroDivisionError = ", type(e))
except TypeError as e:
    print("TypeError = ", type(e))

print('Result = ', result)
print('End')