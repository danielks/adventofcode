import os

with open("teste.txt", "r") as f:
    conteudo = f.readlines()

soma = 0

for v in conteudo:
    num = int(v)
    soma = soma + num

print(soma)

print("teste")