s = "Dimik's"
print(s)

s = 'Dimik\'s'
print(s)



country = "Bangladesh"
print(country[0])
print(country[6])


for c in country:
    print(c)



country = "Bangla" + "desh"
print(country)

x = "50" + "5"
print(x)



country = "Bangladesh"
print(country.find("Ban"))



country = "North Korea"
new_country = country.replace("North", "South")
print(new_country)

text = "this is a test. this is another test. this is final test."
new_text = text.replace("this", "This")
print(new_text)
print(text)



text = " this is a string. "
new_text = text.rstrip()
print(new_text)
new_text = text.lstrip()
print(new_text)



s1 = "Bangladesh"
s_up = s1.upper()
print(s_up)
s_low = s1.lower()
print(s_low)
s_cap = s1.capitalize()
print(s_cap)



str = "I am a programmer."
words = str.split()
print(words)
for word in words:
    print(word)



str = "This is"
print(str.count("is"))



s = "Bangladesh"
print(s.startswith("Ban"))
print(s.endswith("esh"))



name = "Mr. Anderson"
if name.startswith("Mr."):
    print("Dear Sir")



str = "a quick brown fox jumps over the lazy dog"
for c in "abcdefghijklmnopqrstuvwxyz":
    print(c, str.count(c))



import turtle

name = turtle.textinput("name", "What is your name?")
name = name.lower()
if name.startswith("mr"):
    print("Hello Sir, how are you?")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello Madam, how are you?")
else:
    name = name.capitalize()
    str = "Hi " + name + "! How are you?"
    print(str)

turtle.exitonclick()


