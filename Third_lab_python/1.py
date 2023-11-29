with open('number.txt') as numb:
    print(list(map(int, numb.read().split(' '))))