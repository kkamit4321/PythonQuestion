dictonary={"name":"amit",
           "subject":{"phy":50,
                      "che":60,
                      "hindi":80,
                      "math":90}}
# print(dictonary["subject"]["phy"])
# access all key given dictionary
# print(dictonary.keys())
# print(list(dictonary.values()))
a=list(dictonary.items())
print(a[1])
a= ("amit","sumit")
dictonary.update(a)
print(dictonary)