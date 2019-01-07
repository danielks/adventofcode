class Step:
    def __init__(self, nome):
        self.nome = nome
        self.antes_de = ''

steps = []

with open("day7input.txt", "r") as f:
    conteudo = f.readlines()

for c in conteudo:
    nome = c[5]

    jaexiste = False

    for step in steps:
        if step.nome == nome:
            step.antes_de += c[36]
            jaexiste = True
            break
    
    if not jaexiste:
        ns = Step(nome)
        ns.antes_de = c[36]
        steps.append(ns)

steps.sort(key = lambda s: s.nome)

continua = True

while continua:
    nadaMudou = True

    for i in range(len(steps)):
        for j in range(len(steps)):
            if i == j:
                continue

            if i < j:
                if steps[i].nome in steps[j].antes_de:
                    #steps[j], steps[i] = steps[i], steps[j]
                    
                    nadaMudou = False
    
    if nadaMudou:
        break
            

res = ''

for s in steps:
    res += s.nome

res += steps[len(steps)-1].antes_de

print(res)