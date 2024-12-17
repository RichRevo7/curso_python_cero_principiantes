### variables ### 

my_string_variable = 'My String Variable' # es la funcion que deseo que se ejecute.
print(my_string_variable) # es lo que me va imprimir (lo que muestre en la pantalla)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# concatenación de variables en un pint
print(my_string_variable, my_int_to_str_variable, my_bool_variable) # que me imrpima diferentes datos, que esta montado en una cadena.

print('Este es el valor de:', my_bool_variable) # esta concatenando diferente formas.

# Algunas Funciones del sistema.

print(len(my_string_variable)) # lo que hace len, es contar. que my_string_variable = 18 caracteres.

# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = 'Ricardo', 'Revolorio', 'RichRevo7', '36'
print("Me llamo: ", name, surname, "Mi edad es:", age, ". Y mi alias es:", alias)

#Inputs
"""
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')

print(name)
print(age)
"""

# Cambiamos su tipo
name = 35
age = 'Rich'
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = 'Mi direccion'
address = True
address = 5
address = 1.2
print(type(address))


