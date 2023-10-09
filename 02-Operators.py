#round() redonde a numero entero cercano
#round(,1) redonde al decimal mas cercano

##Operadores Aritmeticos##

# Esta son las mas comunes 
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) #Te da el resto
print(3 // 4) # Se llama flor división, da un numero entero, aproxima , no da decimales
print(3 ** 4) #Exponenete 
print(3 ** 4 + 3 / 3 * 3 // 3 ) 

# Con cadenas de texto de puede concatenar

print('Hola ' + 'Python ' + 'que tal')
print('Hola '+ str(5)) # Recordamos str transforma cualquier tipo en string
print('hola' * 5)
print('Hola ' * (5 * 20 )) #Solo de puede con enteros los floats no van es decir los decimales

my_float = 2.5 * 2
print('hola ' * int(my_float))

## Operadores comparativos ##

print( 3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(4 == 4 )
print(3 !=  4) 
print( 3 > 4 == 2)

print( 'hola' > 'Python')
print('hola' < 'Pyhthon')
print('aaa' <= 'aab')
print('aaa' <= 'aab') # Ordenación Alfabetica Asci
print('hola' >= 'Python')
print('hola' == 'Hola' )
print('hola' !=  'Python') 
print(len("aaaa") >= len("abaa")) # Cuenta caracteres

## Operadores logicos ##

print(3 > 4 and 'Hola' > 'Python' )
print(3 > 4 or 'Hola' > 'Python' )
print(3 < 4 and 'Hola' < 'Python' )
print(3 < 4 or ('Hola' > 'Python' and 4 == 4 ))
print(not (3 > 4 ) )

