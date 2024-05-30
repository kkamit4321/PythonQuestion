import sys
n = len(sys.argv)
args = sys.argv
print("number of command line argument=", n)
print("the arg are=", args)
print("the args one by one=")
for a in args:
    print(a)