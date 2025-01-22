# buscar todos casos donde se forme la figura X con las palabras M,A y S
# exemplo:
# M.M
# .A.
# S.S
# sample debería devolver 9 ca

# sample = """.M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........""".strip()
# sample=sample.splitlines()



with open("input", "r") as inputF:
    puzzle=inputF.read().splitlines()

suma=0
for fila,letras in enumerate(puzzle):
    for posic,letra in enumerate(letras):
            if letra=="A" and fila!=0 and posic!=0 and fila+1!=len(puzzle) and posic+1!=len(letras):
                diagonal_1=("A".join([puzzle[fila-1][posic-1],puzzle[fila+1][posic+1]]))
                diagonal_2=("A".join([puzzle[fila-1][posic+1],puzzle[fila+1][posic-1]]))
                
                if diagonal_1 in ["MAS","SAM"] and diagonal_2 in ["MAS","SAM"]:
                    suma+=1


print(suma)