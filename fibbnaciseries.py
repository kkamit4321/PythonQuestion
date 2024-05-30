n = int(input("enter any number"))
def fibbnaci(n):
    if (n == 1)or(n ==0):
        return n
    else:
        n = fibbnaci(n-1)+fibbnaci(n-2)
        return n
fibbnaci(n)
for i in range(n):
    print(fibbnaci(i))

