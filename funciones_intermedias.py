#1
#ACTUALIZAR VALORES EN DICCIONARIOS Y LISTAS

def actualizar_valores():

    #Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
    x = [ [5,2,3], [10,8,9] ]

    x[1][0] = 15
    print(x)



    #Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
    estudiantes = [ {'first_name': 'Michael','last_name': 'Jordan'}, {'first_name': 'John', 'last_name': 'Rosales'} ]

    estudiantes[0]['last_name'] ='Bryan'
    print(estudiantes)



    #En el directorio_deportes, cambia "Messi" por "Andrés".
    directorio_deportes = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
    }

    directorio_deportes['fútbol'][0] = 'Andres'
    print(directorio_deportes)



    #Cambia el valor 20 en z a 30.

    z = [ {'x': 10, 'y': 20} ]

    #z['x'] = 10
    z[0]['y'] = 30
    print(z)

actualizar_valores()
print("--------------")






#2
#ITERAR A TRAVES DE UNA LISTA DE DICCIONARIOS
#Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada 
#diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:

# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for x in range(len(some_list)):
        print(f"first_name - {some_list[x]['first_name']}, last_name - {some_list[x]['last_name']}")

iterateDictionary(estudiantes)
print("--------------")







#3
#Obtener valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list) que, dada una lista de diccionarios y un nombre de clave, 
#la función imprima el valor almacenado en esa clave para cada diccionario.

#Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
#Michael
#John
#Mark
#KB

#Y iterateDictionary2('last_name', estudiantes) debería generar:
#Jordan
#Rosales
#Guillen
#Tonel

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
    print('----------')

iterateDictionary2('first_name',estudiantes)
iterateDictionary2('last_name',estudiantes)
print("--------------")







# 4 Iterar a través de un diccionarios con valores de lista
#Crea una función printInfo(some_dict) que, dado un diccionario cuyos valores son todos listas, 
#imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la 
#lista de cada clave

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for ubic in some_dict:
        print(len(some_dict[ubic]), ubic.upper())

        for instruct in some_dict[ubic]:
            print(instruct)

printInfo(dojo)
