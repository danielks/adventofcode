with open("day2input.txt", "r") as f:
    conteudo_bruto = f.readlines()

conteudo = [c.replace('\n', '') for c in conteudo_bruto]

#apenas para teste
#conteudo = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

def processa(s):
    repetidos2vezes = False
    repetidos3vezes = False

    caracteres_ja_processados = []

    print(s)

    for i in range(len(s)):
        c = s[i]

        if c in caracteres_ja_processados:
            continue

        caracteres_ja_processados.append(c)

        count = 0

        for j in range(i, len(s)):
            if c == s[j]:
                count = count + 1

        if count == 2:
            repetidos2vezes = True
        elif count == 3:
            repetidos3vezes = True

    return repetidos2vezes, repetidos3vezes

total2vezes = 0
total3vezes = 0

for c in conteudo:
    duasvezes, tresvezes = processa(c)

    if duasvezes:
        total2vezes = total2vezes + 1

    if tresvezes:
        total3vezes = total3vezes + 1

print(total2vezes * total3vezes)

#print(conteudo)