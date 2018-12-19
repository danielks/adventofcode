from datetime import datetime

with open("day4input.txt", "r") as f:
    conteudo_bruto = f.readlines()

conteudo = [c.replace('\n', '') for c in conteudo_bruto]

from enum import Enum

class TipoEvento(Enum):
    INICIA_TURNO = 0
    PEGA_NO_SONO = 1
    ACORDA = 2

class Evento:
    def __init__(self, texttoparse):
        self.idguarda = 0
        self.datahora = datetime.strptime(texttoparse[1:17], '%Y-%m-%d %H:%M')

        pos = texttoparse.rfind('Guard #')

        if pos >= 0:
            self.tipo = TipoEvento.INICIA_TURNO

            inicio = pos + 7
            fim = texttoparse.rfind(' begins ')

            self.idguarda = int(texttoparse[inicio:fim])
        else:
            pos = texttoparse.rfind(' falls asleep')

            if pos >= 0:
                self.tipo = TipoEvento.PEGA_NO_SONO
            else:
                pos = texttoparse.rfind(' wakes up')

                if pos >= 0:
                    self.tipo = TipoEvento.ACORDA    

    def __str__(self):
        return "Id: {0}, DataHora: {1}".format(self.idguarda, self.datahora)

class Guarda:
    def __init__(self, id):
        #o indice desse array é o minuto, seu valor é quantas vezes nesse minuto o guarda estava dormindo.
        #ex: minutosdormidos[5] = 3 significa que no minuto 5 da hora, 3 vezes esse guarda estava dormindo
        self.id = id
        self.minutosdormidos = [0 for _ in range(60)]
        self.eventos = []

    def add_evento(self, evento):
        self.eventos.append(evento)
    
    def total_minutos_dormidos(self):
        return sum(self.minutosdormidos)

    def minuto_mais_dormido(self):
        maximo = 0
        res = 0

        for i in range(len(self.minutosdormidos)):
            if self.minutosdormidos[i] > maximo:
                maximo = self.minutosdormidos[i]
                res = i
        
        return res

    def processa_eventos(self):
        minuto_inicio = -1
        minuto_fim = -1

        for e in self.eventos:
            if e.tipo == TipoEvento.PEGA_NO_SONO:
                minuto_inicio = e.datahora.minute
            elif e.tipo == TipoEvento.ACORDA:
                minuto_fim = e.datahora.minute

                #o minuto fim, que é o que acorda, nao conta como dormindo, por isso -1
                for x in range (minuto_inicio, minuto_fim-1):
                    self.minutosdormidos[x] += 1

    def __str__(self):
        return "Guarda - Id: {0}.".format(self.id)


#e1 = Evento('[1518-11-10 23:52] Guard #881 begins shift')
#e2 = Evento('[1518-11-08 00:51] wakes up')
#e3 = Evento('[1518-05-14 00:40] falls asleep')
#eventos = [e1, e2, e3]

eventos = [Evento(c) for c in conteudo]

for v in eventos:
    print(v)

print('eventos ordenados')

eventos.sort(key=lambda e: e.datahora)

ultimoid = 0

for e in eventos:
    if e.tipo == TipoEvento.INICIA_TURNO:
        ultimoid = e.idguarda
    else:
        e.idguarda = ultimoid

guardas = []

def find_guarda_by_id(id):
    for g in guardas:
        if g.id == id:
            return g

    return None

g = None

for e in eventos:

    if (e.tipo == TipoEvento.INICIA_TURNO):
        g = find_guarda_by_id(e.idguarda)

        if g == None:
            g = Guarda(e.idguarda)

            guardas.append(g)
    else:
        g.add_evento(e)


    print(e)

#print(g.minutosdormidos)
#print(len(g.minutosdormidos))

guarda_que_mais_dormiu = None

for g in guardas:
    g.processa_eventos()

    if guarda_que_mais_dormiu == None:
        guarda_que_mais_dormiu = g
    else:
        if g.total_minutos_dormidos() > guarda_que_mais_dormiu.total_minutos_dormidos():
            guarda_que_mais_dormiu = g

    #print(g)
    #print('Eventos:')

    #for e in g.eventos:
    #    print (e.tipo)

    #print("Minuto mais dormido: {0}. Total minutos dormidos: {1}.".format(g.minuto_mais_dormido(), g.total_minutos_dormidos()))
    
    #print(sum([]))

print("Id do guarda que mais dormiu: {0}".format(guarda_que_mais_dormiu.id))
print("Total de minutos dormidos: {0}".format(guarda_que_mais_dormiu.total_minutos_dormidos()))
print("Minuto que mais dormiu: {0}".format(guarda_que_mais_dormiu.minuto_mais_dormido()))