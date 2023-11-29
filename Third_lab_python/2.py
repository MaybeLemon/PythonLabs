a = input()
with open(a) as file:
    kolvo = file.readlines()
    if len(kolvo) >= 5:
        for i in range(5):
            print(str(kolvo[i]), end='')
    else:
        for x in kolvo:
            print(str(x), end='')