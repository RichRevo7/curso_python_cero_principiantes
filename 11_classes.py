### Classes ###

class MyEmptyPerson:
  pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.full_name = f'{name} {surname} ({alias})' # Propiedad publica
        self.__name = name # Propiedad privada
    
    def get_name (self):
        return self.__name

    def walk (self):
        print(f'{self.full_name} Esta Caminando')

my_person = Person('Ricardo', 'Revolorio')
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person('Ricardo', 'Revolorio', 'RichRevo')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Brais Moure (El loco de los perros)'
print(my_other_person.full_name)