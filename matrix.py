r=int(input("enter row value"))
c=int(input("enter column value"))
matrix=[]
for i in range (r):
    a=[]
    for j in range (c):
        a.append(int(input()))
    matrix.append(a)
for i in range (r):
    for j in range (c):
       print(matrix[i][j],end=" ")
    print("\n")
        
# Row = int(input("Enter the number of rows:"))
# Column = int(input("Enter the number of columns:"))

# # Initialize matrix
# matrix = []
# print("Enter the entries row wise:")

# # For user input
# # A for loop for row entries
# for row in range(Row): 
# 	a = []
# 	# A for loop for column entries
# 	for column in range(Column): 
# 		a.append(int(input()))
# 	matrix.append(a)

# # For printing the matrix
# for row in range(Row):
# 	for column in range(Column):
# 		print(matrix[row][column], end=" ")
# 	print()
