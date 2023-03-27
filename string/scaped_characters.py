mensaje = "Hola\nmundo" # Salto de línea
print(mensaje) # "Hola
               # mundo"

mensaje = 'Line1\nLine2\nLine3'
print(mensaje)

mensaje = "Hola\tmundo" # Tabulación
print(mensaje) # "Hola    mundo"

mensaje = "El nombre de mi perro es \"Fido\"" # Comillas dobles
print(mensaje) # "El nombre de mi perro es "Fido""

mensaje = 'El nombre de mi perro es \'Fido\'' # Comillas simples
print(mensaje) # "El nombre de mi perro es 'Fido'"

# Ejemplos

# Ejemplo de comilla simple
cadena = 'Este es un ejemplo de comilla simple: \'Hola mundo!\''
print(cadena)

# Ejemplo de comilla doble
cadena = "Este es un ejemplo de comilla doble: \"Hola mundo!\""
print(cadena)

# Ejemplo de barra invertida
cadena = "Este es un ejemplo de barra invertida: \\"
print(cadena)

# Ejemplo de nueva línea
cadena = "Este es un ejemplo de nueva línea:\nHola\nmundo!"
print(cadena)

# Ejemplo de retorno de carro
cadena = "Este es un ejemplo de retorno de carro:\rHola mundo!"
print(cadena)

# Ejemplo de tabulación horizontal
cadena = "Este es un ejemplo de tabulación:\tHola mundo!"
print(cadena)

# Ejemplo de retroceso
cadena = "Este es un ejemplo de retroceso:\nHola\b\b mundo!"
print(cadena)

# Ejemplo de avance de página (form feed)
cadena = "Este es un ejemplo de avance de página:\nHola\f\f mundo!"
print(cadena)

# Ejemplo de valor octal
cadena = "Este es un ejemplo de valor octal:\141\142\143"
print(cadena)

# Ejemplo de valor hexadecimal
cadena = "Este es un ejemplo de valor hexadecimal:\x61\x62\x63"
print(cadena)

# Ejemplo de caracter Unicode con nombre
cadena = "Este es un ejemplo de caracter Unicode con nombre: \N{GREEK CAPITAL LETTER OMEGA}"
print(cadena)

# Ejemplo de punto de código Unicode básico (4 dígitos hexadecimales)
cadena = "Este es un ejemplo de punto de código Unicode básico: \u03A9"
print(cadena)

# Ejemplo de punto de código Unicode extendido (8 dígitos hexadecimales)
cadena = "Este es un ejemplo de punto de código Unicode extendido: \U000003A9"
print(cadena)

# Ejemplo de alerta
print("Este es un ejemplo de alerta:\a")

# Ejemplo de tabulación vertical
cadena = "Este es un ejemplo de tabulación vertical:\nHola\vMundo!"
print(cadena)
