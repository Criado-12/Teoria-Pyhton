# Variables 

my_variable = 'My String variable'
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)  #transforma un cualquie tipo de valor en string
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False 
print(my_bool_variable)

#concatenacion de variable en un print
(print( my_int_variable, my_int_to_str_variable , my_variable))
print('Este es el valor de:', my_bool_variable)
# Algunas Funciones del sistema

print(len(my_variable)) # Cuentan los letra (string)

#variables en una sola linea. ¡no abusar de esto posibles fallos!
name, surname, alias , age = 'Alejandro', 'Criado','Bell4quit4' , 17
print('Me llamo:', name, surname,'y tengo', age ,'años y mi alias es:',alias )

#Inputs 

#name = input( 'What is your name:')
#age = input('how old are you?:')
#print(name)
#print(age)


# Cambiamos su tipo
name = 35
age = 'Alejandro'
print(name)
print(age)

#¿Forzamos el tipo? 
address: str = 'Mi direción'
address = 32
print(address)