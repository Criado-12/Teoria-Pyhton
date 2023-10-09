## Strings ##

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string)) #cuenta las letras
print(len(my_other_string))

print(my_string + ' - ' + my_other_string)
print(my_string , ' - ' , my_other_string)

my_new_line_string = 'Este es un String\ncon salto de linea'
print(my_new_line_string)

my_tab_line_string = '\tEste es un String con taulación'
print(my_tab_line_string)

my_scape_line_string = '\\tEste es un String \\nescapado'
print(my_scape_line_string)

# Formateo

name , surname , edad  = 'alejandro' , 'Criado', 17

print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, edad))
print('Mi nombre es %s %s y mi edad es %d' %(name,surname,edad)) # Para definir el tipo de formato
print('Mi nombres es' + name + ' ' + surname + ' y mi edad es ' +  str(edad)) #La peor forma
print(f'Mi nombre es {name} {surname} y mi edad es {edad}') #F = Formatea 

# Desempaquetado de caracteres 
language = 'python'
a , b , c, d, e, f= language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2] #Coje en rango tipo de 2 en 2 
print(language_slice)

# revertir

reversed_language = language[::-1]
print(reversed_language)

# Funciones del sistema

print(language.capitalize()) #pone la letra en mayusculas
print(language.upper()) #todo en mayusculo
print(language.count('t')) #cuenta las letras que quieras
print(language.isnumeric()) # te dicesi es un numero
print('1'.isnumeric())
print(language.lower()) # Todo minusculas
print(language.lower().isupper())# te dice si es cierto isupper = mayuscula
print(language.startswith('py'))# Te dice si empiexa por las letras que empieza y te dice verdadero o falso
print(language.title()) #Te pone mayusculas cada primera letra de cada palabra