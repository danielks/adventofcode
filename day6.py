class Ponto:
	def __init__(self, x, y, nome):
		self.x = x
		self.y = y
		self.nome = nome #damos um nome a cada ponto. se não tiver um nome, não é uma coordenada passada, e sim um ponto calculado de proximidade a outro
		self.mais_proximo_de = []
		self.territorio = []

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

def verifica_se_e_coordenada_passada(x, y):
	for p in pontos:
		if p.x == x and p.y == y:
			return True

	return False

pontos_calculados = []

for x in range(minx, maxx+1):
	for y in range(miny, maxy+1):
		if verifica_se_e_coordenada_passada(x, y):
			continue

		menor_dist = 1000000

		pontocalculado = Ponto(x, y, '')

		for p in pontos:
			dist = p.dist(pontocalculado)

			if dist < menor_dist:
				pontocalculado.mais_proximo_de = [p]
				menor_dist = dist
			elif dist == menor_dist:
				pontocalculado.mais_proximo_de.append(p)
		
		if len(pontocalculado.mais_proximo_de) == 1:
			pontocalculado.mais_proximo_de[0].territorio.append(pontocalculado)

		pontos_calculados.append(pontocalculado)
			
pontos.sort(key = lambda p: len(p.territorio), reverse=True)

ponto_com_maior_area_valida = None

for p in pontos:
	#pegamos a maior area que nao seja infinita
	#e como definimos se tem infinito? caso alguma parte de seu territorio esteja na borda que calculamos.
	#obs: aqui já está na ordem de maior pro menor

	if p.x == minx or p.x == maxx or p.y == miny or p.y == maxy:
		continue

	valido = True
	
	for t in p.territorio:
		if t.x == minx or t.x == maxx or t.y == miny or t.y == maxy:
			valido = False
			break
	
	if valido:
		ponto_com_maior_area_valida = p
		break

print('area: {0}'.format(len(ponto_com_maior_area_valida.territorio)+1))


for p in pontos:
	print('x: {0} y: {1}'.format(p.x, p.y))

print(minx)
print(maxx)
print(miny)
print(maxy)

todos_pontos = []
todos_pontos.extend(pontos)
todos_pontos.extend(pontos_calculados)
todos_pontos.sort(key = lambda p: (p.x, p.y))

def find_ponto(x, y):
	for p in todos_pontos:
		if p.x == x and p.y == y:
			return p

text_file = open("output.txt", "w")



for y in range(miny, maxy+1):

	linha = []

	for x in range(minx, maxx+1):
		p = find_ponto(x, y)

		if p is None:
			continue

		s = ''

		if p.nome != '':
			s = p.nome
		else:
			if len(p.mais_proximo_de) > 1:
				s = '..'
			else:
				s = p.mais_proximo_de[0].nome.lower()

		linha.append(s)

	text_file.write(','.join(linha) + '\n')

text_file.close()