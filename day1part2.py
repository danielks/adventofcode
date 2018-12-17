with open("teste.txt", "r") as f:
    conteudo = f.readlines()

soma = 0

frequencias = []

continua = True

while continua:
    for v in conteudo:
        num = int(v)

        soma = soma + num
        

        if soma in frequencias:
            continua = False #para sair do outer loop
            break

        frequencias.append(soma)
        #print(soma)

    print("reinicia " + str(soma))

print(soma)

print("teste")

#CODIGO SUPER LENTO, LEVOU MINUTOS PARA EXECUTAR