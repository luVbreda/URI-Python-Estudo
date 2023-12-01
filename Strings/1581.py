N = int(input())
linguas = []

for i in range(N):
    ingles = False
    pessoas = int(input())
    for j in range(pessoas):
        linguas.append(input())
        if j>1 and linguas[j]!=linguas[j-1]:
            ingles = True
    if ingles:
        print("ingles")
    else:
        print(linguas[0])
    linguas.clear()
    