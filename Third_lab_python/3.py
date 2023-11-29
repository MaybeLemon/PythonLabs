with open(input()) as file:
    kolvo = file.readlines()
    for i in range(1, len(kolvo)+1):
        print(f'{i}: {kolvo[i-1]}', end='')
