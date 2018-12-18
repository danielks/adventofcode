with open("day2input.txt", "r") as f:
    conteudo_bruto = f.readlines()

conteudo = [c.replace('\n', '') for c in conteudo_bruto]

def diff1(s1, s2):
    #retorna True se tem somente diferenca de 1 caracter, na mesma posicao, entre s1 e s2, e caso True,
    #retorna a string sem essa diferenca. Caso False, retorna ""

    if len(s1) != len(s2):
        return False, ""

    diffcount = 0

    pos = 0

    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            diffcount += 1
            pos = i

        if diffcount > 1:
            #ja pode parar
            return False, ""
    
    if diffcount == 1:
        return True, s1[:pos] + s1[(pos+1):]
    
    return False, ""

for i in range(len(conteudo)):
    box1 = conteudo[i]

    res = False
    strres = ""

    for j in range(len(conteudo)):
        box2 = conteudo[j]

        res, strres = diff1(box1, box2)

        if res:
            break

    if res:
        print(strres)
        break


#print(diff1("abcde", "abcde"))

#print(conteudo)