# buscar toos los casos donde se forme la palabra "xmas",
# tanto en diagonal como horizontal como vertical, y en ambos sentidos
# sample debería dedvolver 18 casos

# sample = """....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX""".strip()
# sample=sample.splitlines()

with open("input", "r") as inputF:
    puzzle=inputF.read().splitlines()


xmas=0
for fila,letras in enumerate(puzzle):
    for posic,letra in enumerate(letras):
        if letra=="X" and posic>2 and "".join([letras[posic-1],letras[posic-2],letras[posic-3]]) == "MAS":
            xmas+=1 #izquierda
        if letra=="X" and posic<len(letras)-3 and "".join([letras[posic+1],letras[posic+2],letras[posic+3]]) == "MAS":
            xmas+=1 #derecha
        if letra=="X" and fila>2 and "".join([puzzle[fila-1][posic],puzzle[fila-2][posic],puzzle[fila-3][posic]]) == "MAS":
            xmas+=1 #parriba
        if letra=="X" and fila<len(puzzle)-3 and "".join([puzzle[fila+1][posic],puzzle[fila+2][posic],puzzle[fila+3][posic]]) == "MAS":
            xmas+=1 #pabajo
        if letra=="X" and posic>2 and fila<len(puzzle)-3 and "".join([puzzle[fila+1][posic-1],puzzle[fila+2][posic-2],puzzle[fila+3][posic-3]]) == "MAS":
            xmas+=1 # diagonal izquierda,pabajo
        if letra=="X" and posic>2 and fila>2 and "".join([puzzle[fila-1][posic-1],puzzle[fila-2][posic-2],puzzle[fila-3][posic-3]]) == "MAS":
            xmas+=1 # diagonal izquierda,parriba
        if letra=="X" and posic<len(letras)-3 and fila>2 and "".join([puzzle[fila-1][posic+1],puzzle[fila-2][posic+2],puzzle[fila-3][posic+3]]) == "MAS":
            xmas+=1 # diagonal derecha,parriba
        if letra=="X" and posic<len(letras)-3 and fila<len(puzzle)-3 and "".join([puzzle[fila+1][posic+1],puzzle[fila+2][posic+2],puzzle[fila+3][posic+3]]) == "MAS":
            xmas+=1 # diagonal derecha,pabajo
print(xmas)
