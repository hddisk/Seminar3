def IntoBinary(number):
    binarynumber=""
    if (number!=0):
        while (number>=1):
            if (number %2==0):
                binarynumber=binarynumber+"0"
                number=number/2
            else:
                binarynumber=binarynumber+"1"
                number=(number-1)/2

    else:
        binarynumber="0"

    return "".join(reversed(binarynumber))

num=int(input("Введите число "))
print(IntoBinary(num))