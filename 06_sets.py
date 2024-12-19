### sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {'Ricardo', 'Revolorio', 36}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('MoureDev')

print(my_other_set) # Un set no es una estructura ordenada.

my_other_set.add('MoureDev') # Un set no admite repetidos

print(my_other_set)

print('Revolorio' in my_other_set)
print('Revo' in my_other_set)

my_other_set.remove('Revolorio')
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set =  {'Ricardo', 'Revolorio', 36}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Koltrin', 'Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({'Javascript', 'C#'}))

print(my_new_set.difference(my_set))