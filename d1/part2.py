import os
import sys

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

#aquí con otro bucle while, apuntamos en cada iteracion
#cuantas veces se repite el numero 
while counter < len(right_col):
    l=left_col[counter]
    score=0
    for i in right_col:
        if l==i:
            score+=1
    full_result+=l*score
    counter+=1
print(full_result)

