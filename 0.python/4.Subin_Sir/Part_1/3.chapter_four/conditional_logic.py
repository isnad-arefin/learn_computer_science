numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(numbers[1])
print(numbers[9])
print(numbers[10])



saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka","Maldeep"]
print(saarc)
print(saarc[0])
print("Number of countries in SAARC:", len(saarc))



saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka","Maldeep"]
country = input("Enter the name of the country: ")
if country in saarc:
    print(country, "is a member of SAARC")
else:
    print(country, "is not a member of SAARC")
print("Program terminated")



marks = input("Please enter your marks: ")
marks = int(marks)

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
else:
    grade = "F"

print("Your grade is", grade)



number = float(input("please enter your number: "))

if number < 0:
    print("The entered number is negative.")
elif number > 0:
    print("The entered number is positive.")
elif number == 0:
    print("The entered number is zero.")



num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number. ")
else: print("This is an even number. ")



n1 = 50
n2 = 60
n3 = 65

if n1 > n2:
    max_n = n1
else:
    max_n = n2

if n3 > max_n:
    max_n = n3

print("Maximum : ", max_n)








