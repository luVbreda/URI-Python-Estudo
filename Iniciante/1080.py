maior = 0

for j in range(100):
    numero = int(input())
    if(numero>maior):
        maior = numero
        posicao = j+1

print(maior)
print(posicao)