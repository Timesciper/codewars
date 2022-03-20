# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

def next_bigger(n):
    str_n = list(str(n))
    min_num = 10
    current_index = 0
    for i in range(1, len(str_n)+1):
        element = int(str_n[-i])
        if element < min_num:
            changer = str_n[-current_index]
            print('changed {} for {}'.format(element, changer))
            str_n[-current_index] = str(element)
            str_n[-i] = changer
            break
        if element > min_num:
            print(element<min_num)
            print('lower with {} as min and {} as element'. format(min_num, element))
            current_index = i
            min_num = element
    res_str = ''
    for i in str_n:
        res_str += i
    return int(res_str)
