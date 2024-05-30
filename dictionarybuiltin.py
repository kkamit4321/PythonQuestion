dictionary1={'amit':2, 2:4, 3:5, 5:'amit', 4:5, 6:'sumit'}
print(dictionary1,type(dictionary1))
# len() it helps to find length of dictionary
print(len(dictionary1))
# string representation of dictionary
print(str(dictionary1))
# copy() it function used to create copy of original dictionary
print(dictionary1.copy())
# keys() function helps to check all key in dictionary
print(dictionary1.keys())
# values() it helps to access all data of dictionary
print(dictionary1.values())
# items() function return list to dictionary with key:value pairs
print(dictionary1.items())
# update() helps to change the data of dictionary
dictionary2={12:'amrit'}
dictionary1.update(dictionary2)
print(dictionary1)
# # has_key() it helps to check key has or not in dictionary
# dictionary1.has_key('amit')
# print(dictionary1)
# ger() it helps to access value using key in dictionary
print(dictionary1.get('amit'))
# pop() it is used to remove key:value in dictionary
dictionary1.pop('amit')
print(dictionary1)
# print(dictionary1.push())
# clear() it used to remove all data of dictionary
print(dictionary1.clear())
print(dict(dictionary1))
