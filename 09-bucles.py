### Bucles ###

#while

my_condition = 0


while my_condition <10:   #Se repite segun una condición
    print(my_condition)
    my_condition += 1
else: #es opcional 
    print('Mi condición es mayor o igual que 10')

while my_condition <20:
    my_condition += 1
    if my_condition == 15:
        print('Se detiene la ejecución')
        break

    print(my_condition)
        
    


print('La ejecución continua')


#For

my_list = [35, 24, 62, 52, 30, 30 , 17]

for elemt in my_list:  #Se repite tantas veces segun elementos tengamos

    print(elemt)

my_tuple = (35, 1.77, 'Alejandro' , 'Criado' , 'Alejandro')

for elemt in my_tuple:  #Se repite tantas veces segun elementos tengamos

    print(elemt)

my_set = {'Alejandro','Criado', 17}

for elemt in my_set:  #Se repite tantas veces segun elementos tengamos

    print(elemt)

my_dicct = {'Nombre':'Alejandro', 'Apellido':'Criado','Edad':17, 1:'Python'}

for elemt in my_dicct:  #Se repite tantas veces segun elementos tengamos
    print(elemt)
    if elemt == 'Edad':
        break #Nos salimos del toodo no llegmaos al print
    print('se ejecuta')

else:
    print('El bucle for para mi diccionario ha finalizad')

for elemt in my_dicct:  #Se repite tantas veces segun elementos tengamos
    print(elemt)
    if elemt == 'Edad':
        continue # Vuelve el for  sin ejecutar lo que hay debajo
    print('se ejecuta')
else:
    print('El bucle for para mi diccionario ha finalizad')



