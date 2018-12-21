#contarq = 'dabAcCaCBAcCcaDA'

with open("day5input.txt", "r") as f:
    contarqbruto = f.readlines()

contarq = contarqbruto[0]

def polaridades_reversas(c1, c2):
    return c1.upper() == c2.upper() and ord(c1) != ord(c2)

def processa(conteudo):
    i = 0

    while i < len(conteudo)-1:
        c = conteudo[i]

        seguinte = conteudo[i+1]

        if polaridades_reversas(c, seguinte):
            conteudo = conteudo[:i] + conteudo[i+2:]

            if i > 0:
                i = i - 1
        else:
            i += 1

    return len(conteudo)

import time
start_time = time.time()

unidades = {}

for c in contarq:
    if c.upper() not in unidades:
        unidades[c.upper()] = processa(contarq.replace(c.upper(), '').replace(c.lower(), ''))

menorvalor = (2**32)-1

for k, v in unidades.items():
    if v < menorvalor:
        menorvalor = v

#print(len(processa(contarq)))
#print(conteudo)
#print(unidades)
print(menorvalor)

print("Esse processo levou %s segundos" % (time.time() - start_time))