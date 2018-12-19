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
        self.tipo = TipoEvento.INICIA_TURNO
        self.datahora = datetime.strptime(texttoparse[1:17], '%Y-%m-%d %H:%M')

    def __str__(self):
        return "Id: {0}, DataHora: {1}".format(self.idguarda, self.datahora)


e1 = Evento('[1518-11-10 23:52] Guard #881 begins shift')
e2 = Evento('[1518-11-08 00:51] wakes up')
e3 = Evento('[1518-05-14 00:40] falls asleep')

eventos = [e1, e2, e3]

for v in eventos:
    print(v)

print('eventos ordenados')

eventos.sort(key=lambda e: e.datahora)

for v in eventos:
    print(v)