# calcular la diferencia de los mínimos en cada columna del input y sumarla
# usar el contenido en sample de referencia, en este caso, es 1-3, 2-3, 3-3, 3-4, 3-5, 4-9
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

# separar la lista en ambas columnas
for a in location_IDs:
    left_col.append(int(a.split(   )[0]))
    right_col.append(int(a.split(   )[-1]))

result=0

# diferencia de los minimos en cada columna en cada iteracion
while len(left_col)>0:
    l=left_col.pop(left_col.index(min(left_col)))
    r=right_col.pop(right_col.index(min(right_col)))
    result+=abs(r-l)
print(result)
