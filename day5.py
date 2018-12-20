conteudo = 'dabAcCaCBAcCcaDA'

with open("day5input.txt", "r") as f:
    conteudo_bruto = f.readlines()

conteudo = conteudo_bruto[0]

def polaridades_reversas(c1, c2):
    return c1.upper() == c2.upper() and ord(c1) != ord(c2)


continua = True
while continua:
    for i in range(len(conteudo)):
        c = conteudo[i]

        if i < len(conteudo)-1:
            seguinte = conteudo[i+1]

            if polaridades_reversas(c, seguinte):
                conteudo = conteudo[:i] + conteudo[i+2:]
                break
        else:
            continua = False


            


        #print(c)

print(len(conteudo))