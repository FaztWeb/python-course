# concatenation
"hello " + "world"

# print("hello " + 1) # error
"hello " * 10

# join

palabras = ["Hola", "mundo", "desde", "Python"]
separador = " "
mensaje = separador.join(palabras)
print(mensaje) # "Hola mundo desde Python"

# F-string

nombre = "Juan"
edad = 30
mensaje = f"Mi nombre es {nombre} y tengo {edad} años"
print(mensaje) # "Mi nombre es Juan y tengo 30 años"

# format

nombre = "Juan"
edad = 30
mensaje = "Mi nombre es {} y tengo {} años".format(nombre, edad)
print(mensaje) # "Mi nombre es Juan y tengo 30 años"
