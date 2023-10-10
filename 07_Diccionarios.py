### Diccionarios ###

my_dict = dict()
my_other_dicct = {}

print(type(my_dict))
print(type(my_other_dicct))

my_other_dicct = {'Nombre':'Alejandro', 'Apellido':'Criado','Edad':17, 1:'Python'}

my_dict ={
    'Nombre':'Alejandro',
    'Apellido':'Criado',
    'Edad':17,
    'Lenguajes':{'Python','Swift','kotlin'},
     1: 1.68
      }
    
print(my_other_dicct)
print(my_dict)

print(len(my_other_dicct))
print(len(my_dict))

print(my_dict['Nombre'])

my_dict['Nombre'] = 'Roberto' #Modificamos lo que esta previamente, me sigue o no me sigue

print(my_dict['Nombre'])

print(my_dict[1])

my_dict['Calle'] = 'Calle criado' #Añadimos un nuevo valor

print(my_dict)

del my_dict['Calle'] #Eliminar elemento en el diccionario

print(my_dict)

print('Criado' in my_dict)
print('Apellido' in my_dict)

print(my_dict.items()) #Nos muestra todo el diccionario, listado de cada uno de los items
print(my_dict.keys()) #Lista de keys , identificadores
print(my_dict.values()) #Lista de valores

my_list = ['Nombre', 1, 'Piso']

my_new_dict = dict.fromkeys((my_list)) # Se crea un dicconario nuevo si valores, ESTO ES UNA CACA POCO PRACTICO
print(my_new_dict)
my_new_dict= dict.fromkeys(('Nombres', 1, 'Pisos'))
print(my_new_dict)
my_new_dict= dict.fromkeys((my_dict)) #Copia el diccionario pero solo con las llaves
print(my_new_dict)
my_new_dict= dict.fromkeys(my_dict,('Criado','Alejandro')) #Le hemos metido a todos los elemtos lo que pongamos en los paranttesis
print(my_new_dict)
my_new_dict= dict.fromkeys(my_dict,['Criado','Alejandro']) #Le hemos metido a todos los elemtos lo que pongamos en los corchetes es decit listas en todos
print(my_new_dict)
my_new_dict= dict.fromkeys(my_dict, 'Alejandro en todos lados') #Le hemos metido a todos los elemtos lo que pongamos en los corchetes es decit listas en todos
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))
print(list(my_new_dict.values())) #Nos dicce los valores asignados ya que llamamos a los valores en una lista
print(list(my_new_dict)) #Si lo transformamos en lista solo se quedan las llaves
print(tuple(my_new_dict)) #Si lo transformamos en tuplas solo se quedan las llaves
print(set(my_new_dict)) #Si lo transformamos en set solo se quedan las llaves y desordenado ya que los sets son desordeados

