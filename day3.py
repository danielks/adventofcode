with open("day3input.txt", "r") as f:
    conteudo_bruto = f.readlines()

conteudo = [c.replace('\n', '') for c in conteudo_bruto]

class FabricPiece:
    def __init__(self, text_to_parse):
        posarroba = text_to_parse.rfind(' @')

        self.id = int(text_to_parse[1:posarroba])

        posdoispontos = text_to_parse.rfind(': ')

        aux = text_to_parse[posarroba+3:posdoispontos]
        
        auxsplit = aux.split(',')

        self.x = int(auxsplit[0])
        self.y = int(auxsplit[1])

        aux = text_to_parse[posdoispontos+2:]
        auxsplit = aux.split('x')
        self.largura = int(auxsplit[0])
        self.altura = int(auxsplit[1])

    def area(self):
        return self.largura * self.altura

    def areacomum(self, fp):
        #retorna o tanto de área comum entre dois pedaços
        #caso não tenham área em comum, retorna 0

        esquerda = max(self.x, fp.x)
        direita = min(self.x + self.largura, fp.x + fp.largura)
        baixo = min(self.y + self.altura, fp.y + fp.altura)
        topo = max(self.y, fp.y)

        if (esquerda < direita) and (topo < baixo):
            return (direita - esquerda) * (baixo - topo)

        return 0

    def pontosemcomum(self, fp):
        res = []
        #retorna os "pontos" em comum entre dois retangulos. na verdade não são pontos, mas ok
        esquerda = max(self.x, fp.x)
        direita = min(self.x + self.largura, fp.x + fp.largura)
        baixo = min(self.y + self.altura, fp.y + fp.altura)
        topo = max(self.y, fp.y)

        if (esquerda < direita) and (topo < baixo):
            for x in range(esquerda, direita):
                for y in range(topo, baixo):
                    res.append([x, y])

        return res

pieces = []
pontosrepetidos = []

for c in conteudo:
    fp = FabricPiece(c)
    pieces.append(fp)

    #print(fp.id)
    #print(fp.x)
    #print(fp.y)
    #print(fp.largura)
    #print(fp.altura)

fp1 = FabricPiece("#1 @ 0,0: 2x2")
fp2 = FabricPiece("#2 @ 0,0: 2x2")
#pieces = [fp1, fp2]

print(fp1.pontosemcomum(fp2))

#alem de ser horrivelmente lento, nao funciona
totalarea = 0

maxX = 0
maxY = 0

for v in pieces:
    if v.x + v.largura > maxX:
        maxX = v.x + v.largura

    if v.y + v.altura > maxY:
        maxY = v.x + v.altura

pontosrepetidos = [[0 for x in range(maxX)] for y in range(maxY)] 

for i in range(len(pieces)):
    print('i: %s' % i)
    for j in range(i+1, len(pieces)):
        #print('j: %s' % j)
        totalarea += pieces[i].areacomum(pieces[j])

        

        pontosemcomum = pieces[i].pontosemcomum(pieces[j])

        for v in pontosemcomum:
            pontosrepetidos[v[0]][v[1]] = 1

        #for v in pontosemcomum:
        #    if v not in pontosrepetidos:
        #        pontosrepetidos.append(v)
    


print(len(pontosrepetidos))
print(pontosrepetidos)

somatotal = 0

for v1 in pontosrepetidos:
    for v2 in v1:
        somatotal += v2

print(somatotal)