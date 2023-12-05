for e in range(20):
    K, L = map(int, input().split())
    if K == 0 and L == 0:
        break;
    divisor = 2
    while K%divisor!=0 and divisor <= L:
        divisor+=1
    if divisor >= L:
        print("GOOD")
    else:
        print("BAD",divisor)