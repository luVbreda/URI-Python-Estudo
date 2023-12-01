N = int(input())
postagens = []

postagens.extend(map(int, input().split()))
postagens.sort()

if N%2 == 1:
    print(postagens[int(N/2)])
else:
    print(int((postagens[int(N/2)]+postagens[int(N/2)-1])/2))