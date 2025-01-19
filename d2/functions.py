def checker_asc(given_chain):
    result="Safe" # result devolverá safe si no encontramos error
    p=-1
    for a in given_chain:
        if int(p)>int(a): # comprobar si cada carqacter es mayor que el anterior
            result="Unsafe"
            break
        elif abs(int(p)-int(a))>3 and p!=-1: # comprobar la diferencia con cada caracter (evitar el caso de p=-1 al principio del bucle)
            result="Unsafe"
            break
        elif p==a: # comprobar si no son iguales
            result="Unsafe"
            break
        p=a
    return result
       
# <<<<<misma funcion de arriba pero invertida>>>>>
def checker_des(given_chain):
    result="Safe"
    p=-1
    for a in given_chain:
        if int(p)<int(a) and p!=-1: # evitamos el caso de p=-1
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


def string_solvener(given_chain, dir):
    if dir=="des":
        result=checker_des(given_chain) # si desciende o asciende, llamamos a la función necesaria
        p=-1
        if result=="Unsafe":
            for ind,a in enumerate(given_chain):
                if int(a)>int(p) and p!=-1: 
                    # dos sublistas por error, eliminando actual y anterior numero
                    sol_one=given_chain.copy() # se usa .copy para no modificar la cadena en la referencia
                    del sol_one[ind]
                    sol_two=given_chain.copy()
                    del sol_two[ind-1]
                    if checker_des(sol_one) == "Safe": # comprobamos ambas soluciones, si una da "Safe", y rompemos bucle
                        result=checker_des(sol_one)
                        break
                    elif checker_des(sol_two) == "Safe":
                        result=checker_des(sol_two)
                        break
                elif abs(int(a)-int(p))>3 and p!=-1:
                    sol_one=given_chain.copy()
                    del sol_one[ind]
                    sol_two=given_chain.copy()
                    del sol_two[ind-1]
                    if checker_des(sol_one) == "Safe":
                        result=checker_des(sol_one)
                        break
                    elif checker_des(sol_two) == "Safe":
                        result=checker_des(sol_two)
                        break
                elif int(a)==int(p):
                    sol_eq=given_chain.copy()
                    del sol_eq[ind]
                    if checker_des(sol_eq) == "Safe":
                        result=checker_des(sol_eq)
                        break
                p=a
    elif dir=="asc":
        result=checker_asc(given_chain)
        p=-1
        if result=="Unsafe":
            for ind, a in enumerate(given_chain):
                if int(a)<int(p) and p!=-1:
                    sol_one=given_chain.copy()
                    del sol_one[ind]
                    sol_two=given_chain.copy()
                    del sol_two[ind-1]
                    if checker_asc(sol_one) == "Safe":
                        result=checker_asc(sol_one)
                        break
                    elif checker_asc(sol_two) == "Safe":
                        result=checker_asc(sol_two)
                        break
                elif abs(int(a)-int(p))>3 and p!=-1:
                    sol_one=given_chain.copy()
                    del sol_one[ind]
                    sol_two=given_chain.copy()
                    del sol_two[ind-1]
                    if checker_asc(sol_one) == "Safe":
                        result=checker_asc(sol_one)
                        break
                    elif checker_asc(sol_two) == "Safe":
                        result=checker_asc(sol_two)
                        break
                elif int(a)==int(p):
                    sol_eq=given_chain.copy()
                    del sol_eq[ind]
                    if checker_asc(sol_eq) == "Safe":
                        result=checker_asc(sol_eq)
                        break
                p=a
    return result