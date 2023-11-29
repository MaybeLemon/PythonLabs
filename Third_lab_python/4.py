summ = 0
with open('names.txt') as file:
    kolvo = file.readlines()
    for x in kolvo:
        summ += len(x.split(' '))
print(summ)