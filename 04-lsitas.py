## Listas ##

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30 , 17]


print(len(my_list))

my_other_list = [35, 1.68, 'alejandro', 'Moure'] #Se empieza a contar desde 0#

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
#print(my_other_list[4]) error
#print(my_other_list[-5]) error

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]

print(age)

print(my_list + my_other_list)
#print(my_list + my_other_list) error

my_other_list.append('Elale') #Inserta nuevo valor al final
print(my_other_list)

my_other_list.insert(1, 'rojo')#inserta lo que le digas en la posición que le digas
print(my_other_list)

my_other_list[1] = 'verde' 
print(my_other_list)

my_other_list.remove('verde') #Elimina lo que le digas
print(my_other_list)

my_list.remove(30)# el primer dato del mismo tipo
print(my_list)

my_list.pop() # Elimina el ultimo dato # mira para abajo de dudas que esto es como quierass
print(my_list.pop())
print(my_list)

print(my_list.pop(1))
print(my_list)

my_pop_element = my_list.pop(1)
print(my_pop_element)

my_new_list = my_list.copy()

del my_list[1] #borra la posición que le indicas
print(my_list)

my_list.clear()
print(my_list)

print(my_list)
print(my_new_list)

my_new_list.reverse() #imprime los valores alreves
print(my_new_list)

my_new_list.sort() #ordena de mayor a menor o de lo que te de la gana
print(my_new_list)

print(my_new_list[1:2])

my_list = 'Hola Python'
print(my_list)
print(type(my_list))

