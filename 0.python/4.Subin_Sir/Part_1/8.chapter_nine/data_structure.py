saarc = [ "Bangladesh", "India", "Sri Lanka"]
print(saarc)
saarc.append("Pakistan")
print(saarc)



saarc.sort()
print(saarc)
li = [1, 3, 7, 2, 4, 6]
li.sort()
print(li)
li.reverse()
print(li)



fruits = ["mango", "banana", "orange"]
fruits.insert(0, "apple")
print(fruits)


fruits = ['apple', 'mango', 'coconut', 'banana', 'orange']
fruits.remove("coconut")
print(fruits)
item = "pineapple"
if item in fruits:
    remove(item)
else:
    print(item, "not in list")



print(fruits)
item = fruits.pop(1)
item = "orange"
print(fruits)



li = [1, 2, 3]
li2 = [3, 4, 5, 6]
li.extend(li2)
print(li)
print(li.count(3))
print(li)
del(li[1])
print(li)



li = []
for x in range(10):
    li.append(x)
print(li)



li1 = [1, 2, 3]
li2 = [4, 5, 6]
li = li1 + li2
print(li)




li1 = [1, 2, 3]
li2 = li1 * 3
print(li2)



li = ["a", "b", "c"]
print(li)
str = "".join(li)
print(str)
str = ",".join(li)
print(str)
str = " - ".join(li)
print(str)



li = [1, 2, 3, 4]
new_li = [2 * x for x in li]
print(new_li)



even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)



items = (1, 2, 5.5, ["a", "b","c"], ("apple", "mango"))
for item in items:
    print(item, type(item))
print(items[3][0])


tpl = (1, 2, 3)
li = list(tpl)
print(li)


A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 8}
C = A & B
print(C)
C = A | B
print(C)
C = A ^ B
print(C)
C = A - B
print(C)
C = B - A
print(C)



# marks = [77, 76, 65, 78, 62, 64, 60, 77, 75, 79]
# roll = input("Please enter your roll number:")
# print("your mark is", marks[int(roll)-1])



marks = [[74, 73], [70, 75], [68, 72], [73, 73]]
print(marks[0])


marks = {1: 77, 2: 76, 5: 62, 4: 78, 3: 65}
print(type(marks))
print(marks[3])


dt = {"a": "A", "b": "B", "c": "C"}
dt[1, 2, 3] = "tuple"
print(dt)