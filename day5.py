#otimizado. levava uns 100 segundos para rodar, agora leva aprox 0,22s

conteudo = 'dabAcCaCBAcCcaDA'

with open("day5input.txt", "r") as f:
    conteudo_bruto = f.readlines()

conteudo = conteudo_bruto[0]

def polaridades_reversas(c1, c2):
    return c1.upper() == c2.upper() and ord(c1) != ord(c2)

import time
start_time = time.time()

continua = True

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

print(len(conteudo))
print(conteudo)

print("Esse processo levou %s segundos" % (time.time() - start_time))