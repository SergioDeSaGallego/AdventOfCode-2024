# ahora, buscar cada mul y calcular las sumas como antes
# cada don't() en la cadena inhabilitará todas las multiplicaciones consiguientes
# que cada do() las habilitará otra vez
# sample="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+don't()mul(32,64](mul(11,8)undo()?mul(8,5))"

import re

with open("input","r") as inputF:
    memory=inputF.read()


pattern=r"mul\(\d+,\d+\)"
# encuentra ocurrencias de do() y dont()
do_ocurrencias=list(re.finditer(r"do\(\)", memory))
dont_ocurrencias=list(re.finditer(r"don't\(\)", memory))



lista_do=[]
lista_dont=[]

# almacenar posiciones iniciales de cada ocurrencia (re.finditer guarda el span(posicion) y el dato encontrado
for a in do_ocurrencias:
    lista_do.append(list((a.start(),"do")))
for a in dont_ocurrencias:
    lista_dont.append(list((a.start(),"dont")))

# encuentra y almacena los mul(*,*)
list_mul=list(re.finditer(pattern,memory))
tentativa_mul=[]
for a in list_mul:
    tentativa_mul.append(list((a.start(),a[0])))

lista_final=[]

# ordenamos cada ocurerncia por posicion
while lista_do or lista_dont or tentativa_mul:
    #obtenemos el primer elemento de cada lista o infinito si está vacia, usamos la psocion mas baja
    if lista_do!=[]:
        mindo=lista_do[0]
    else:
        mindo=list((float("inf"),"ept"))
    if lista_dont!=[]:
        mindont=lista_dont[0]
    else:
        mindont=list((float("inf"),"ept"))
    if tentativa_mul!=[]:
        minmul=tentativa_mul[0]
    else:
        minmul=list((float("inf"), "ept"))
    
    fullmin=min(mindo,mindont,minmul)
    if fullmin == mindo:
        lista_final.append(lista_do.pop(0))
    elif fullmin == mindont:
        lista_final.append(lista_dont.pop(0))
    elif fullmin == minmul:
        lista_final.append(tentativa_mul.pop(0))

# recorremos la lista final haciendo la operacion solo con state activado
sum=0
state="ACTIVATED"
for case in lista_final:
    if case[1]=="do":
        state="ACTIVATED"
    elif case[1]=="dont":
        state="DEACTIVATED"
    elif state=="ACTIVATED":
        a=case[1].strip("mul(").strip(")").split(",")[0]
        b=case[1].strip("mul(").strip(")").split(",")[1]
        sum+=int(a)*int(b)


print(sum)



