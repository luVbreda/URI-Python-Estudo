C = int(input())

for i in range(C):
    notas = []
    maior = 0
    notas.extend(map(int, input().split()))
    media=sum(notas[1:])/notas[0]
    for j in range(1, notas[0]+1):
        if notas[j]>media:
            maior+=1

    porcet = "{:.3f}".format((maior/notas[0])*100)
    print(f"{porcet}%")
    notas.clear()