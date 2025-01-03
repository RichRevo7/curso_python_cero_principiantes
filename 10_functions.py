### Functions ###

# Las funciones son bloques de código que se pueden ejecutar múltiples veces, con diferentes argumentos.
# Las funciones se definen con la palabra clave "def" seguida del nombre de la función y los paréntesis.
# Los argumentos se pasan a la función entre los paréntesis.

def my_function():
    print('Esto es una funcion')

my_function()
my_function()
my_function()

def sum_two_values(frist_value, second_value):
    print(frist_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values('5', '7')
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(frist_value, second_value):
    my_sum = frist_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f'{name} {surname}')

print_name(surname ='Revolorio', name = 'Ricardo')

def print_name_with_default (name, surname, alias = 'sin alias'):
    print(f'{name} {surname} {alias}')

print_name_with_default('Ricardo', 'Revolorio')
print_name_with_default('Ricardo', 'Revolorio', 'RichRevo')

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())


print_upper_texts('Hola', 'python', 'RichRevo')
print_upper_texts('Hola')