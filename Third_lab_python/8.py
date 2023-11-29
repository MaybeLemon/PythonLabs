with open('file.txt') as file:
    temp = file.read().split(' ')
    print(*temp)
    print(f'Сумма чисел: {sum(list(map(int, temp)))}\n'
          f'Количество чисел: {len(temp)}')