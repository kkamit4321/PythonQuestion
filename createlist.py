# creating a empty list using list() method and directly
mylist1=[]
mylist2=list()
print(mylist2,type(mylist2))
print(len(mylist1))
# create a list of size n
n=int(input("enter any number"))
for i in range(1,n+1):
    print(i)
# create list from 1 to n using list comprehesion
n=12
output=[i for i in range(1,n+1)]
print(output)
# create list in list put string values
mylist3=['banana','potato','tomato']
print(mylist3)
# crete list using object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Student objects
student1 = Student('Arjun', 14)
student2 = Student('Ajay', 15)
student3 = Student('Mike', 13)

# Create list with objects
x = [student1, student2, student3]
print(x)

