### Tuples ###

my_tuple = tuple()
my_other = ()

my_tuple = (35, 1.77, 'Alejandro' , 'Criado' , 'Alejandro')
my_other = (35,60,30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) Error
#print(my_tuple[-6]) Error
print(my_tuple.count('Alejandro')) #Busca en la tupla las coincidencias
print(my_tuple.index('Criado'))
print(my_tuple.index('Alejandro'))

#my_tuple[1] = 1.68 no se puede modificar las tuplas
my_sum_tuple = my_tuple + my_other
print(my_sum_tuple)

print(my_sum_tuple[3:6])

#tupla en lista
my_tuple = list(my_tuple)

print(type(my_tuple))

my_tuple[4] = 'MoureDev'
my_tuple.insert(1, 'Verde')
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] esto no se puede lass tuplas no se modifcan¡¡¡¡¡

del my_tuple #elimina la tupla
#print(my_tuple) destruye la tupla