from itertools import chain
def longest_words(file):
    lst = []
    file = file.read()
    for x in file.split('\n'):
        lst = list(chain(lst, x.split(' ')))
    for i in range(len(lst)):
        lst[i] = [lst[i].lower(), len(lst[i])]
    lst.sort(key=lambda x: x[1], reverse=True)
    maxx = lst[0][1]
    for y in lst:
        if y[1] != maxx:
            break
        print(y[0])

with open ('article.txt', 'r', encoding='UTF-8') as file:
    longest_words(file)