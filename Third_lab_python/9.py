summ = 0
countt = 0
try:
    with open('number.txt') as file:
        kolvo = file.readlines()
        for x in kolvo:
            try:
                temp = list(map(int, x.split(' ')))
            except:
                print('Не удалось конвертировать число')
                exit()
            summ += sum(temp)
            countt += len(x.split(' '))
except IOError:
    print('Ошибка чтения файла')
    exit()
print(summ/countt)
