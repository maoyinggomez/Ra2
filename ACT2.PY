
#Acitividad 2
celcius= int(input("Ingresa la temperatura en Celcius para convertir en Fahrenheit: "))
fah= float(input("Ingresa la temperatura en fahrenheit para convertir en celcius: "))

conveCel= celcius*1.8 +32
conveFah=(5/9)*(fah-32)

print(f"La temperatura en Fahrenheit es:{conveCel}")
print(f"La temperatura en Celcius es:{fah}")
