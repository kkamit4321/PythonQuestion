set1={1,2,3,4,5,6,7,'amit','sumit',7,6,9,'amrit'}
# enumerate() it return enumerate object it contains the index and value of all the items of set as a pair
print(enumerate(set1))
# any() it tells the have data or not
set2={}
print(any(set1),any(set2))
# add() and update() it helps to add new item in set
set2={1,2,3,4,5,6,1,7,'amit','sumit',7,6,9,'amrit'}
set2.add('kk')
print(set2)
# remove() and discard() it helps to delete single data
set2.remove(1)
print(set2)
# pop() function return deleting after top(first) element set
set1={1,2,3,4,5,6,7,'amit','sumit',7,6,9,'amrit'}
print(set1.pop())
# union() it is used two set and create new set with unique value
set3={1,2,3,4,5,6,7,'amit','sumit',7,6,9,'amrit'}
set4={55,6,87,999,'pk',854,4,5,6,7,'amit','sumit',7,6,9,'kk','mk','sk'}
set5=set3.union(set4)
print(set5)
# intersection() it is used two set and create new set with common value
set6=set3.intersection(set4)
print(set6)
# difference() it is used two or more sets into a new set then after print olny first set value
set7={1,2,6,7,'amit','sumit',9999,7,6,9,'amrit'}
set8={1,2,3,4,5,6,7,'amit',7,6,9,'amrit'}
set9={1,2,3,4,5,6,7,'sumit',7,6,9}
set10=set7.difference(set8,set9)
print(set10)
# issubset() and issuperset() it return boolean answer
set11={1,2,3,4,5,6,7,'amit','sumit',7,6,9,'amrit'}
set12={1,2,7,'amit','sumit',7,6,9,'amrit'}
set13=set11.issubset(set12)
print(set13)