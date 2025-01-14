from functions import checker_asc,checker_des

# sample="""7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""
# sample=sample.splitlines()

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
