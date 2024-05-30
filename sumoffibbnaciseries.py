n = int(input("enter any number"))
def fibbnaci(n):
    if (n == 1)or(n ==0):
        return n
    else:
        n = fibbnaci(n-1)+fibbnaci(n-2)
        s=0
        s=s+n
        return s
fibbnaci(n)
print(s)
for i in range(n):
    # s = s + fibbnaci(i)
    print(fibbnaci(i))