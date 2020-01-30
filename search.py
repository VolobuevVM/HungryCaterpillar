"""модуль поиска"""

def substr_in_str(str, substr):
    """функция поиска подстроки в строке. Собственная"""

    #список позиций вхождений подстроки
    nums = []
    for i in range(0, len(str) - 1):
        #ищем вхождение первого символа подстроки
        if substr[0] == str[i]:
            #проходим по подстроке
            shift = 0 #сдвиг
            for j in range(1, len(substr) - 1):
                #если следующий символ не совпадает - 
                if substr[j] != str[i + j]:
                    #проверка - а встречается ли еще первый символ подстроки 
                    #в куске строки длиной подстроки
                    for k in range(j, len(substr) - 1):
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


#функция поиска на алгоритме Бойера-Мура

def boyer_moore(source, template):
    offset_table ={}
    nums = []
    source_len = len(source)
    template_len = len(template)

    if template_len > source_len:
        return -1

    for i in range(0, 256):
        offset_table[chr(i)] = template_len

    for i in range(0, template_len - 1):
        offset_table[template[i]] = template_len - i - 1

    i = template_len - 1
    j =i
    k = i

    
    while j >= 0 and i <= source_len - 1:
        j = template_len - 1
        k = i
        while j >= 0 and source[k] == template[j]:
            k = k - 1
            j = j - 1
        i = i + offset_table(source[i])
        nums.append(k+1)
       
    occurrences = tuple(nums)

    return occurrences

    #функция двоичного поиска


    #функция поиска по хэш-функции