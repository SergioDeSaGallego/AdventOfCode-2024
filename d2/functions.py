def checker_asc(cadena):
    copy_cadena=cadena.copy()
    result="Safe"
    p=-1
    for a in copy_cadena:
        if int(p)>int(a):
            result="Unsafe"
            break
        elif abs(int(p)-int(a))>3 and p!=-1:
        # el primer caso siempre podrá dar errores con esta parte, de ahi el "and p!=-1"
            result="Unsafe"
            break
        elif p==a:
            result="Unsafe"
            break
        p=a
    return result
       

def checker_des(cadena):
    copy_cadena=cadena.copy()
    result="Safe"
    p=-1
    for a in copy_cadena:
        if int(p)<int(a) and p!=-1:
        # el primer caso siempre podrá dar errores con esta parte, de ahi el "and p!=-1"
            result="Unsafe"
            break
        elif abs(int(p)-int(a))>3 and p!=-1:
            result="Unsafe"
            break
        elif p==a:
            result="Unsafe"
            break
        p=a
    return result


def string_solvener(cadena, dir):
    solving_cadena=cadena.copy()
    if dir=="des":
        result=checker_des(solving_cadena)
        p=-1
        if result=="Unsafe":
            for ind,a in enumerate(solving_cadena):
                if int(a)>int(p) and p!=-1:
                    sol_one=solving_cadena.copy()
                    del sol_one[ind]
                    sol_two=solving_cadena.copy()
                    del sol_two[ind-1]
                    if checker_des(sol_one) == "Safe":
                        result=checker_des(sol_one)
                        break
                    elif checker_des(sol_two) == "Safe":
                        result=checker_des(sol_two)
                        break
                elif abs(int(a)-int(p))>3 and p!=-1:
                    sol_one=solving_cadena.copy()
                    del sol_one[ind]
                    sol_two=solving_cadena.copy()
                    del sol_two[ind-1]
                    if checker_des(sol_one) == "Safe":
                        result=checker_des(sol_one)
                        break
                    elif checker_des(sol_two) == "Safe":
                        result=checker_des(sol_two)
                        break
                elif int(a)==int(p):
                    sol_eq=solving_cadena.copy()
                    del sol_eq[ind]
                    if checker_des(sol_eq) == "Safe":
                        result=checker_des(sol_eq)
                        break
                p=a
    elif dir=="asc":
        result=checker_asc(solving_cadena)
        p=-1
        if result=="Unsafe":
            for ind, a in enumerate(solving_cadena):
                if int(a)<int(p) and p!=-1:
                    sol_one=solving_cadena.copy()
                    del sol_one[ind]
                    sol_two=solving_cadena.copy()
                    del sol_two[ind-1]
                    if checker_asc(sol_one) == "Safe":
                        result=checker_asc(sol_one)
                        break
                    elif checker_asc(sol_two) == "Safe":
                        result=checker_asc(sol_two)
                        break
                elif abs(int(a)-int(p))>3 and p!=-1:
                    sol_one=solving_cadena.copy()
                    del sol_one[ind]
                    sol_two=solving_cadena.copy()
                    del sol_two[ind-1]
                    if checker_asc(sol_one) == "Safe":
                        result=checker_asc(sol_one)
                        break
                    elif checker_asc(sol_two) == "Safe":
                        result=checker_asc(sol_two)
                        break
                elif int(a)==int(p):
                    sol_eq=solving_cadena.copy()
                    del sol_eq[ind]
                    if checker_asc(sol_eq) == "Safe":
                        result=checker_asc(sol_eq)
                        break
                p=a
    return result