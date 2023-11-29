summ = 0
with open('number.txt') as file:
    kolvo = file.readlines()
    for x in kolvo:
        summ += sum(list(map(int, x.split(' '))))
print(summ)