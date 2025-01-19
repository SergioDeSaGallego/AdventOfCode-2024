# buscar todas las ocurrencias de "mul(*,*)", multiplicar cada una y sumar todos los resultados
# sample="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

import re

with open('input', 'r') as inputF:
    memory=inputF.read()

pattern=r"mul\(\d+,\d+\)"
# buscar todas las ocurrencias que cumplan con la expresion regular de arriba
finder=list(re.finditer(pattern,memory))


sum=0
for a in finder:
    fixed=a[0].strip("mul(").strip(")")
    sum += int(fixed.split(",")[0]) * int(fixed.split(",")[1])
print(sum)

