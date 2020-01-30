"""модуль поиска"""

def substr_in_str(str, substr):
    """функция поиска подстроки в строке. Собственная"""

    #список позиций вхождений подстроки
    nums = []
    for i = 0 to len(str) - 1:
        #ищем вхождение первого символа подстроки
        if substr[0] == str[i]:
            #проходим по подстроке
            shift = 0 #сдвиг
            for j = 1 to len(substr) - 1:
                #если следующий символ не совпадает - 
                if substr[j] != str[i + j]:
                    #проверка - а встречается ли еще первый символ подстроки 
                    #в куске строки длиной подстроки
                    for k = j to len(substr) - 1:
                        #если встречается - устанавливаем величину сдвига на этот символ
                        if substr[0] == str[i + k]:
                            shift = k
                            break
                    #если этот цикл успешен - ни один символ куска строки 
                    #не равен первому символу подстроки. Значит сдвиг равен длине подстроки + 1
                    else:
                        shift = len(substr) + 1
                        break
            #если этот цикл успешен, то подстрока найдена. Записываем её в массив и
            #сдвигаемся на длину подстроки + 1 (вариант, когда одинаковые подстроки в строке
            # могут быть с разницей в 1...длина_подстроки символ нас не интересует)
            else:
                nums.append(i)
                shift = len(substr) + 1
        #если первый символ подстроки не равен текущему символу строки,
        #то сдвигаемся на 1
        else:
            shift = 1
        #делаем сдвиг
        i = i + shift

    #преобразуем массив в кортеж и возвращаем его
    occurrences = tuple(nums)

    return occurrences


#функция поиска на алгоритме Кнута-Морриса-Пратта

def knuth_morris_pratt (text, pattern):
    nums = []
    pattern = tuple(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            nums.append(startPos)

    occurrences = tuple(nums)

    return occurrences