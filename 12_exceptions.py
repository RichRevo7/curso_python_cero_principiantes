### Exceptions Handling ###
# The try block lets you test a block of code for errors.
# Exceptions are errors that occur during the execution of a program. When that error occurs, Python generates an exception that can be handled, which avoids your program to crash.

numberOne = 5
numberTwo = 1
#numberTwo = '1'

# try except

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except:
    # Se ejecuta si se produce una excepción
    print('Se ha producido un error')

# try except else finally

try:
    print(numberOne + numberTwo)
except: 
    print('Se ha producido un error')
else: # Opcional
    # Se ejecuta si no se ha producido una excepción
    print('La ejecucion continua Correctamente')
finally:# Opcional
    #se ejecuta siempre
    print('La ejecucion continua')

# Exceptiones por tipo

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError:
    print('Se ha producido un error')
except TypeError:
    print('Se ha producido un error')

# Captura de la informacion de la excepción

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError as error:
    print(error)
except Exception as Exception:
    print(Exception)
