def proizvedenie(nmbrs):
    index = 0
    if (n%2 == 0):
        index = int(n/2)
    else:
        index = int(n/2+1)
    proizv = [0]*index
    for i in range(index):
        proizv[i]=nmbrs[i]*nmbrs[-i-1]
    print(proizv)

from random import randint
n = int(input("Введите размерность "))
numbers = [0]*n
for i in range(n):
    numbers[i] = randint(0, 10)
print(numbers)
proizvedenie(numbers)