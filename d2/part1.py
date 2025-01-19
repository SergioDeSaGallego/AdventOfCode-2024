# Al reporte recivido, cada línea será "correcta" si:
# cada línea es una sucesion ascendente o descendente
# ningún número tiene una diferencia de más de 3 y respecto al anterior
# habrá que devolver el número de líneas correctas
# en el ejemplo:

# sample="""7 6 4 2 1   correcta
# 1 2 7 8 9             incorrecta (2 7) incrementa 5
# 9 7 6 2 1             incorrecta (6 2) decrementa 4
# 1 3 2 4 5             incorrecta (3 2) decrementa en libnea ascendente
# 8 6 4 4 1             incorrecta (4 4) dos iguales
# 1 3 6 7 9"""          correcta
# sample=sample.splitlines()


from functions import checker_asc,checker_des

with open('input', 'r') as inputF:
    reports=inputF.read().splitlines()
    


count=0
for report in reports:
    report=report.split(" ")
    if int(report[0]) > int(report[-1]):
        result=checker_des(report)
    elif int(report[0]) < int(report[-1]):
        result=checker_asc(report)
    
    if result=='Safe':
        count+=1

print(count)
