N = int(input())

for i in range(N):
    x, y = input().split()

    tamanho = len(x)-len(y)
    ne = False
    if tamanho < 0:
        print("nao encaixa")
    else:
        for e in range(len(y)):
            if x[len(x)-e-1] != y[len(y)-e-1]:
                print("nao encaixa")
                ne = True
                break
        if not ne:
            print("encaixa")