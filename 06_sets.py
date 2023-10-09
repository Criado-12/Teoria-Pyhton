### Sets ###

my_sets = set() #tipo de dato
my_other_set = {}

print(type(my_sets))
print(type(my_other_set)) #Esto nos dice que inicialmente es un dicionario

my_other_set = {'Alejandro','Criado', 17}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('Criadiño')

print(my_other_set) #Un set nos es una estructura ordenada

my_other_set.add('Criadiño') #Un set no admite repetidos

print(my_other_set)

print('Alejandro'in my_other_set) #Compruebas si existen dichos datos en el set
print('Ala'in my_other_set)

my_other_set.remove('Criado')
print(my_other_set)

my_other_set.clear() #borra los datos de dentro
print(len(my_other_set))

del my_other_set #Nos lo cargamos por que queremos. Del es funcion dell sistema no del set
#print(my_other_set)

my_set = {'Alejandro','Criado', 17}
my_list = list(my_set)
print(my_set)
print(my_list[0])

my_other_set = {'Kotline','Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({'JavaScript', 'C#'})) #El ultimo union es solo en est alinea ya que no esta almacenado

print(my_new_set.difference(my_set)) #Te muestra solo lo diferente