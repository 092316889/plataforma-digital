#calcular el area y perimetro de un triangulo equilatero sin saber su altura

import math
n_1 = 0
n_1 = int(input('ingrese un lado del triangulo equilatero: \n '))
perimetro = n_1 + n_1 + n_1 
print('el perimetro de su triangulo es:')
print (perimetro)
area = n_1**2 - n_1 
pita = math.sqrt(area)
print('la altura es es:')
print(pita)
area_a = n_1 * pita / 2
print ('el area es:')
print (area_a)
