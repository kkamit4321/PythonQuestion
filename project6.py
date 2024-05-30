from math import pow
y=0
Y=0
e=2
print("------------------------------------------------------------")
print("press 1 for metric conversion\npress 2 for imperial conversion\npress 3 metric to imperial conversion\nimperial to matric conversion")
print("------------------------------------------------------------")
n=int(input("input choice="))
while True:
    if n==1:
        print("press 1 for km to other(m,cm,milimeter,micrometer,nanometer,pico meter)\npress 2 for m to (km,cm,milimeter,micrometer,nanometer,pico meter)\npress 3 for cm to (m,km,milimeter,micrometer,nanometer,pico meter,)\npress 4 for milimeter to (m,cm,km,micrometer,nanometer,pico meter)\npress 5 for nanometer to (m,cm,milimeter,micrometer,km,pico meter)\npress 6 for picometer to (m,cm,milimeter,micrometer,nanometer,km meter)")
        print("------------------------------------------------------------")
        option=int(input("enter choice="))
        if option==1:
            km=float(input("enter value in km="))
            print("meter=",km*1000,"\n","centimeter=",km*100*1000,"\n","milimeter=",km*1000000,"nanometer=",km*1000*1000*1000,"\n","picometer=","\n",km*1000*1000*1000*1000)
        elif option == 2:
            m=float(input("enter value in meter"))
            print("kilo meter=",m/1000,"\n","centimeter=",m*100,"\n","milimeter=",m*1000,"nanometer=",m*1000*1000*1000,"\n","picometer=","\n",m*1000*1000*1000*1000)
        elif option == 3:
            cm=float(input("enter value in centimeter="))
            print("meter=",cm/100,"\n","kilo meter=",cm/(100*1000),"\n","milimeter=",cm*10,"nanometer=",cm*pow(e,5),"\n","picometer=","\n",cm*1000*1000*1000*10)
    x=input("do you continiue y/n")
    if x==y or x==Y:
        n=int(input("input choice="))