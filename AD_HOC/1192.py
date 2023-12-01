N = int(input())

for i in range(N):
    expressao = input()

    if(expressao[0]==expressao[2]):
        print(int(expressao[0])*int(expressao[2]))
    else:
        if(expressao[1].isupper()):
            print(int(expressao[2])-int(expressao[0]))
        else:
            print(int(expressao[0])+int(expressao[2]))