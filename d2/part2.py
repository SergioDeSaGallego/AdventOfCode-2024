# ahora, cada cadena podrá "arreglarse"
# para arreglar una cadena solo se podrá eliminar un número cualquiera de esta

# sample="""7 6 4 2 1   correcta
# 1 2 7 8 9             incorrecta en cualquier caso
# 9 7 6 2 1             incorrecta en cualquier caso
# 1 3 2 4 5             correcta si eliminamos el 3
# 8 6 4 4 1             correcta si eliminamos uno de los 4
# 1 3 6 7 9"""          correcta
# reports=sample.splitlines()


from functions import string_solvener


with open('input', 'r') as inputF:
    reports=inputF.read().splitlines()


count=0
for report in reports:
    counter_asc=0
    counter_des=0
    report=report.split(" ")
    p=-1
    for a_ch in report: # comprobar si la cadena esta ascendiendo o descendiendo
        if int(a_ch)>int(p) and p!=-1: 
            counter_asc+=1
        elif int(a_ch)<int(p) and p!=-1:
            counter_des+=1
        p=a_ch
    if counter_asc>counter_des: 
        result=string_solvener(report, "asc")
    elif counter_asc<counter_des:
        result=string_solvener(report, "des")
    else:
        result="Unsafe"
        
    if result=='Safe':
        count+=1
print(count)
