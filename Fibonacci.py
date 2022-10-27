cont0=0
cont1=1
cont2=1
num=int(input("Ingrese un número. ")) 
if num==0:
    print(cont0)
elif num==1:
    print(cont0)
    print(cont1)
else:
    print(cont0) 
    print(cont1)
    print(cont1)
    for i in range(num-2):
        cont1+=cont2 
        cont2=cont1-cont2
        print(cont1)