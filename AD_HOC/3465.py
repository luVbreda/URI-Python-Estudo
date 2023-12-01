import math

a, b, c = map(int, input().split())

print(f"{math.sqrt(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c)):.3f} m2")