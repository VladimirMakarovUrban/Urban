def djons(num):
    list_num = list(range(1, 21))
    result = []
    for i in list_num:
        for j in list_num:
            if (num % (list_num[i - 1] + list_num[j - 1]) == 0
                    and list_num[i - 1] < list_num[j]
                    and list_num[i - 1] != list_num[j-1]):
                result.append(i)
                result.append(j)
    print(''.join(map(str, result)))


num = int(input('Введите число от 3 до 20: '))
djons(num)
