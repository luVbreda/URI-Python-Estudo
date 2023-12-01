a, b = map(int, input().split())
jogos = []
score = 0

for i in range(a):
    jogos.extend(map(int, input().split()))
    jogos.sort()
    if(jogos[0]!=0):
        score+=1
    jogos.clear()

print(score)