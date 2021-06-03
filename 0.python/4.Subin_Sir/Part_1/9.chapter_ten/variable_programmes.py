# import random
# print(random.random())
#
# print(random.randint(20, 40))


# import turtle
# print(turtle.position())
# turtle.forward(100)
# print(turtle.position())
# turtle.left(90)
# print(turtle.position())
# turtle.forward(50)
# print(turtle.position())


# import turtle
# import random
#
# colors = ["red", "green", "blue", "yellow", "orange", "black", "purple"]
# turtle.penup()
#
# for i in range(20):
#     x = random.randint(-200, 200)
#     y = random.randint(-200, 200)
#     turtle.setposition(x, y)
#     i = random.randint(0, len(colors)-1)
#     turtle.dot(colors[i])
#
# turtle.done()



# import random
#
# number = random.randint(1, 1000)
# attempts = 0
#
# while True:
#     input_number = input("Guess the number (between 1 and 1000):")
#     input_number = int(input_number)
#     attempts += 1
#
#     if input_number == number:
#         print("Yes, your guess is correct!")
#         break
#     if input_number > number:
#         print("Incorrect! Please try to guess a smaller number.")
#     else:
#         print("Incorrect! Please try to guess a larger number.")
# print("You tried", attempts, "times to find the correct number.")



# import random
#
# number = random.randint(1, 1000)
# attempts = 0
# low = 1
# high = 1000
# while True:
#     print("Guess the number (between 1 and 1000): ")
#     input_number = (low + high) // 2 # only integer division
#     print("My guess is", input_number)
#     attempts += 1
#
#     if input_number == number:
#         print("Yes, your guess is correct!")
#         break
#     if input_number > number:
#         print("Incorrect! Please try to guess a smaller number.")
#         high = input_number - 1
#     else:
#         print("Incorrect! Please try to guess a larger number.")
#         low = input_number + 1
#
# print("You tried", attempts, "times to find the correct number.")


