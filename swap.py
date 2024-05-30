a = int(input("enter first nubmer"))
b = int(input("enter second number"))
# using two variable
a=a+b
b=a-b
a=a-b
print("a=", a)
print("b=", b)
# using three variable
temp = a
a = b
b = temp
print("a=", a)
print("b=", b)