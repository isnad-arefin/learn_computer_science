# def is_prime3(n):
#     if n == 2:
#         return True # 2 is prime
#     if n % 2 ==0:
#         print(n, "is divisible by 2")
#         return False # all even numbers except 2 are not prime
#     if n < 2:
#         return False # numbers less than 2 are not prime
#     prime = True
#     for x in range(3, n, 2):
#         if n % x == 0:
#             print(n, "is divisible by", x)
#             prime = False
#             return prime
#     return prime
#
# while True:
#     number = input("Please enter a number (enter 0 to exit): ")
#     number = int(number)
#     if number == 0:
#         break
#     prime = is_prime3(number)
#     if prime is True:
#         print(number, "is a prime number.")
#     else:
#         print(number, "is not a prime number.")
#
#
#
# import math
#
# def is_prime4(n):
#     if n < 2:
#         return False
#     if n== 2:
#         return True
#     if n % 2 == 0:
#         return False
#     m = math.sqrt(n)
#     m = int(m) + 1
#     for x in range(3, m, 2):
#         if n % x ==0:
#             return False
#     return True
# while True:
#     number = input("Please enter a number (enter 0 to exit): ")
#     number = int(number)
#     if number == 0:
#         break
#     prime = is_prime4(number)
#     if prime is True:
#         print(number, "is a prime number.")
#     else:
#         print(number, "is not a prime number.")



import math

def is_prime4(n=1013):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = math.sqrt(n)
    m = int(m) + 1
    for x in range(3, m, 2):
        if n % x ==0:
            return False
    return True

def is_prime_3(n=1013):
    if n == 2:
        return True # 2 is prime
    if n % 2 == 0:
        return False # all even numbers except 2 are not prime
    if n < 2:
        return False # numbers less than 2 are not prime
    prime = True
    for x in range(3, n, 2):
        if n % x == 0:
            prime = False
            return prime
    return prime

import timeit
t1 = timeit.timeit(is_prime_3)
t2 = timeit.timeit(is_prime4)
print(t1, t2, t1/t2)
