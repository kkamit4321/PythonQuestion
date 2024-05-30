# a = {1322241: {'anuj', 'pk', '12345678'}, 1322242: {'rahul', 'praveen kumar', '87654321'}, 1322290: {'mandeep', 'bettiah', '13579123'}}
m = {}
print("choose option")
x = int(input("press 1 for insert data\npress 2 for delete data\npress 3 for show all data:-"))

match x:
    case 1:
        a = input("enter name")
        b = input("enter father name")
        c = input("enter roll no=")
        print(dict(rollno=c, name=a, fname=b))
        # print(a[1322241])
        print("data insert")
    # case 2:
    #     print(a[1322242])
    # case 3:
    # print(dict(rollno=c, name=a, fname=b))