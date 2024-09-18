
#Actividad 3
texto= input("Ingrese una linea de texto: ")
may= texto.upper()
ora= texto.capitalize()
longi= len(texto)
py= "python" in texto
print(f"tiene{longi} caracteres")
print(may)
print(ora)
print(f"La palabra python está?:{py}")