pula = 0

while True:
    try:
        ano = int(input())
        bisexto = hulu = False

        if pula:
            print()
        pula = 1
        if (ano%4==0 and ano%100!=0) or ano%400==0:
            print("This is leap year.")
            bisexto = True
        if ano%15==0:
            print("This is huluculu festival year.")
            hulu = True
        if bisexto and ano%55==0:
            print("This is bulukulu festival year.")
        if not bisexto and not hulu:
            print("This is an ordinary year.")
        print()
    except EOFError:
        break