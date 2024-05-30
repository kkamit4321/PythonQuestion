# numbers = [1, 2, 3, 4, 5]
# squared = [x ** 2 for x in numbers]
# print(squared)
# for i in range([numbers]):
#     print(i)

list1=[1,2,3,4,"amit",4,'sumit','amrit']
# append function helps to add new value
list1.append(10)
print(list1)
list2=[3,5,6,3,7,4,4]
# sort function helps to arrenge elements in ao & do
list2.sort()
print(list2)
# reverse fun helps to reverse the all elements
list2.reverse()
print(list2)
# insert fun helps to add elements as particular location
list2.insert(2,'krishna')
print(list2)
# list slicing(break the all elements)
list3=[1,2,'sumit',3,3,5,'amrit',5,4]
# put all elements comes after that index
print(list3[2:])
# put all elements comes before that index
print(list3[:2])
# in this slicining put beg,end,step
print(list3[2:8:2])
# count fun helps to count all elements
print(list3.count(3))
print(list3[::2])
# # remove fuction it helps to remove the all or particular elements in list
print(list3.remove(2))
print(list3)
# exted() method add to string array
list1.extend(list2)
print(list1)
# sum() it is used to add all elements given in list
list4=[2,4,3,5,2,8,5,8]
print(sum(list4))
# len() it helps to find number exist is list
print(len(list4))
# index() function it function used to find the index of any number
list5=[2,4,3,5,2,8,5,8]
print("index=",list5.index(2))
# min() helps to find minimum value of list
list5=[2,5,3,4,7,8,4,7,4,7,9]
print(min(list5))
list5=['a','C','c','AMit','sumit']
print(min(list5))
# max() it is used to find maximum value in list
list5=[2,5,3,4,7,8,4,7,4,7,9]
print(max(list5))