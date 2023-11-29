summ = 0
countt = 0
with open('number.txt') as file:
    kolvo = file.readlines()
    for x in kolvo:
        summ += sum(list(map(int, x.split(' '))))
        countt += len(x.split(' '))
print(summ/countt)
