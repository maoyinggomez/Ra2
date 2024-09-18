#Actividad 4

edad= int(input("Ingrese su edad: "))
ed= edad >=18
if edad <18:
    print(f"No es mayor de edad, su edad es: {edad}")
elif edad >= 18:
    print(f"Es mayor de edad, su edad es:{edad}")
print(ed)