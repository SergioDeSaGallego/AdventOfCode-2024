

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

#añadimos cada lado de la columna a su respactiva lista
for a in location_IDs:
    left_col.append(int(a.split(   )[0]))
    right_col.append(int(a.split(   )[-1]))

counter=0
full_result=0

#con un bucle while, pillamos en cada iteracion el mínimo
#de cada lista, lo eliminamos de esta, y hacemos la operación
#hasta que no quedan números
while counter < len(left_col):
    r=min(right_col)
    l=min(left_col)
    left_col.remove(l)
    right_col.remove(r)
    result = l-r
    full_result+=abs(result)
print(full_result)



