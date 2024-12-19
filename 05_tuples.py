### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (36, 1.78, 'Ricardo', 'Revolorio', 'Ricardo')
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count('Ricardo'))
print(my_tuple.index('Revolorio'))
print(my_tuple.index('Ricardo'))

#my_tuple[5] = 1.80 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'Mouredev'
my_tuple.insert(1, 'azul')
print(tuple(my_tuple))

#del my_tuple[1] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined