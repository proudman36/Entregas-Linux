def numeroPrimo(num):
	if num==1:
		mensaje="El número no es primo"
	elif num==2:
		mensaje="El número es primo"
	else:
		for i in range(2,num): #9 
			residuo=num%i
			if residuo==0:
				mensaje="El número no es primo"
				break
			else:
				mensaje="El número es primo"
	return mensaje

print(numeroPrimo(int(input("Ingrese un número "))))
