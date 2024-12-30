### Loops ###

# While 

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print('Mi condición es mayor o igual a 10')

print ('La ejecución continua')

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Se detiene la ejecución')
        break
    print(my_condition)

print('La ejcución continua')

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (36, 1.78, 'Ricardo', 'Revolorio', 'Ricardo')

for element in my_tuple:
    print(element)

my_set =  {'Ricardo', 'Revolorio', 36}

for element in my_set:
    print(element)

my_dict = {'Nombre': 'Ricardo', 'Apellido': 'Revolorio', 'Edad':36, 1:'Python'}

for element in my_dict:
    print(element)
    if element == 'Edad':
        break
else:
    print('El bluce for para diccionario ha finalizado')

print('La ejecución continua')

for element in my_dict:
    print(element)
    if element == 'Edad':
        continue
    print('Se ejecuta')
else:
    print('El bluce for para diccionario ha finalizado')

'''for element in my_dict.values():
    print(element)'''