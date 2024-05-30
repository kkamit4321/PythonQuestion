tuple1=(2,4,3,2,3,5,2,8,5,4,25)
# update and insert means change the data in tuple
tuple2=list(tuple1)
tuple2[3]='amit'
tuple3=tuple(tuple2)
print(tuple3, type(tuple3))

# accessing the tuple data
tuple1=(2,4,3,2,3,5,2,8,5,4,25)
print(tuple1[1])

# delete mean delete the all data of data using del()
del tuple1
# tuple1=(2,4,3,2,3,5,2,8,5,4,25)
print(tuple1)
# without parathensis tuple is called tuple packing
tuple4=(2,4,5,3,5)
print(tuple4)

