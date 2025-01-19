# el mismo imput que parte 1
# ahora, hay que calcular cuantas veces cada numero de la izquierda aparece en la columna derecha, multiplicar ese numero por las veces que aparezca, y sumar el resultado
# en este caso, 3x3+4x1+2x0+1x0+3x3+3x3=31

#sample="""3   4
#4   3
#2   5
#1   3
#3   9
#3   3"""
#sample=sample.splitlines()

with open('input', 'r') as inputF:
    location_IDs=inputF.read().splitlines()

#creamos las columnas
left_col  = []
right_col = []

for a in location_IDs:
    left_col.append(int(a.split(   )[0]))
    right_col.append(int(a.split(   )[-1]))

counter=0
full_result=0

#apuntar en cada iteracion cuantas veces se repite el numero y hacer la suma
while counter < len(right_col):
    l=left_col[counter]
    score=0
    for i in right_col:
        if l==i:
            score+=1
    full_result+=l*score
    counter+=1
print(full_result)

