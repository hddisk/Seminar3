def Maxmin(lst):
    max = 0
    min = 1
    for i in range(len(lst)):
        if lst[i]>max:
            max = lst[i]
        if (lst[i]<min and lst[i]!=0):
            min = lst[i]
    return max - min

numbers = [1.1, 1.2, 3.1, 5, 10.01]
list =[0]*len(numbers)
for i in range(len(numbers)):
    list[i]=round(numbers[i]%1,2)
print(list)
print(Maxmin(list))