###Operadores Arimeticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3 + 3  - 7 / 1 // 4)

print('hola ' + 'python ' + '¿Que tal?')
print('hola' + str(5))
print('hola ' * (2 ** 3))

my_float = 2.5 * 2
print('Hola ' * int(my_float))

### operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(4 == 4)

print('hola' > 'python')
print('hola' < 'python')
print('hola' >= 'zola') # Ordenación alfabética.
print('hola' <= 'python')
print('hola' == 'hola')
print('aaaa' >= 'abaa') #Ordenación alfabética por ASCII
print(len('aaaa') >= len('abaa')) #Cuenta caracteres

### Operadores Lógicos ###

print(3 > 4 and 'Hola' > 'python')
print(3 > 4 or 'Hola' > 'python')
print(3 < 4 and 'Hola' < 'python')
print(3 < 4 or 'Hola' < 'python')
print(3 < 4 or ('Hola' > 'python' and 4 == 4))
print(not(3 > 4))