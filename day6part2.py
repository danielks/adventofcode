class Ponto:
    def __init__(self, x, y, nome):
        self.x = x
        self.y = y
        self.nome = nome #damos um nome a cada ponto. se não tiver um nome, não é uma coordenada passada, e sim um ponto calculado de proximidade a outro
        self.mais_proximo_de = []
        self.territorio = []
        self.total_distancias = 0

    def dist(self, p):
        return abs(self.x - p.x) + abs(self.y - p.y)

with open("day6input.txt", "r") as f:
    conteudo = f.readlines()

pontos = []

minx = 100000000
maxx = 0
miny = 100000000
maxy = 0

for i in range(len(conteudo)):
	separado = conteudo[i].split(', ')

	x = int(separado[0])

	y = int(separado[1])

	if x < minx:
		minx = x

	if x > maxx:
		maxx = x

	if y < miny:
		miny = y

	if y > maxy:
		maxy = y

	n = ''

	if i > 26:
		n = 'B' + chr(ord('A')+(i-26))
	else:
		n = 'A' + chr(ord('A')+i)
	
	pontos.append(Ponto(x, y, n))

def find_ponto(x, y):
	for p in pontos:
		if p.x == x and p.y == y:
			return p

	return None

def fast_find_ponto(x, y):
    #so pode usar essa funcao com o grid ja completamente preenchido e ordenado corretamente
    pass

for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        #primeiro preenche todos os pontos do grid
        ponto = find_ponto(x, y)

        if ponto is None:
            ponto = Ponto(x, y, '')
            pontos.append(ponto)

pontos.sort(key = lambda p: (p.y, p.x))

res = []

for p in pontos:
    for p2 in pontos:
        if p2.nome == '':
            continue

        p.total_distancias += p.dist(p2)

    if p.total_distancias < 10000:
        res.append(p)

print(len(res))