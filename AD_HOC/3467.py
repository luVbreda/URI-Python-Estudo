while True:
    try:
        sofa = input()
        if sofa[2] == 'L':
            print("Esse eh o meu lugar")
        else:
            print("Oi, Leonard")
    except EOFError:
        break