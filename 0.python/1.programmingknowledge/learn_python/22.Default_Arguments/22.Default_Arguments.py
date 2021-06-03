
def student(name, age, **marks):
    print("name: ", name)
    print('age', age)
    print('marks', marks)
    for key, value in marks.items():
        print(key, ' ', value)

student('tom', 22, english=95, math=70, physics=80, biology=50)