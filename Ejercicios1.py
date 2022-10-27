email=input("Ingrese un correo electrónico ")
for i in email:
    while email[0]=="@" or email[len(email)-1]=="@" or email.count("@")>1 or email.count("@")<1:
        email=input("Ingrese un email adecuado ")
    


