N = int(input())

for i in range(N):
    x, y = input().split()
    
    palavra = []

    for e in range(len(x) if len(y) > len(x) else len(y)):
        palavra.append(x[e])
        palavra.append(y[e])
        final = e
    
    if len(y) > final:
        for e in range(final+1, len(y)):
            palavra.append(y[e])
    if len(x) > final:
        for e in range(final+1, len(x)):
            palavra.append(x[e])

    for e in range(len(palavra)):
        print(palavra[e], end="")
    print()