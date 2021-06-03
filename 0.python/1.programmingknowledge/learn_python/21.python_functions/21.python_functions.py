def sum(arg1, arg2):
    if type(arg1) != type (arg2):
        print("Please give the args of same type")
        return
    return (arg1 + arg2)

a = sum(15,60)
print(a)
print(sum('Hello ', 'World'))
print(sum(15.647, 80.258))
print(sum("hello", 15))


