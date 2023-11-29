from random import randint
lst = []
for i in range(int(input())):
    lst.append(str(randint(1, 500)))
with open('file.txt', 'w') as file:
    file.write(' '.join(lst))

