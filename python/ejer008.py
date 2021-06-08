# string y mas
esto_es_un_string = 'hola'
esto_es_otro_string = 'mundo'
#como concatenar
print (esto_es_un_string + " " + esto_es_otro_string) #saldra unido hola mundo

#COMO hacer mayuscula la letra
print(esto_es_un_string.upper())
#COMO hacer minuscula la letra
print(esto_es_otro_string.lower())
#COMO hacer para poner solo la primer letra mayuscula
print(esto_es_un_string.capitalize())
#COMO hacer mayuscula la letra
print(esto_es_un_string.title())
# para ver la longitud de la palabra
print(len(esto_es_un_string))
#buscar una caracter y muestra su ubicacion en indice
print(esto_es_otro_string.find('o'))
#rebanar o slice
print(esto_es_otro_string[0:3]) # tu le dices por donde inicie
print(esto_es_otro_string[:3]) #el asume automatico que inicia de 0
print(esto_es_otro_string[1:3])# de que rango a que rango elijo 
# radar
print(esto_es_otro_string[:: -1])

