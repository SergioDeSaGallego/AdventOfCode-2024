from functions import string_solvener

# sample="""7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""
# reports=sample.splitlines()

with open('input', 'r') as inputF:
    reports=inputF.read().splitlines()


count=0
# for report in reports:
#     report=report.split(" ")
#     if int(report[0]) > int(report[-1]):
#         result=checker_v2(report, "des")
#     elif int(report[0]) < int(report[-1]):
#         result=checker_v2(report, "asc")
#         # print(report[0],report[-1],"asc")
#     else:
#         result="Unsafe"
#     if result=='Safe':
#         count+=1
# print(count)


count=0
for report in reports:
    counter_asc=0
    counter_des=0
    report=report.split(" ")
    p=-1
    for a_ch in report:
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