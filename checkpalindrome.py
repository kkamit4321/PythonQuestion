a = int(input("enter number"))
print("enter elements")
for i in range(a):
    b=list(input())
c=b.copy()
d=c.reverse()
print(type(c))
if c==b:
    print("palindrome")
else:
    print("not palindrome")