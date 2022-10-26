pala=input("Ingrese una palabra: ")
palaInv=""
for i in range(len(pala)-1,-1,-1):#El último argumento nos dice de a cuanta cantidad va recorriendo la lista, es decir, si se le pone un 2, va recorriendo la lista de 2 en 2.
    palaInv+=pala[i]
    
if palaInv==pala:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo")