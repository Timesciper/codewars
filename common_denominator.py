#  https://www.codewars.com/kata/54d7660d2daf68c619000d95/train/python
#  ссылка на кату
from functools import reduce

def devide(number):
    #  функция разбирает число на простейшие множители
    if number == 0:
        return [0]
    if number == 1:
        return [1]
    current_number = number
    multiply = 1
    res_list = []
    while multiply <= current_number:
        if multiply == 1:
            multiply += 1
            continue
        if current_number % multiply == 0:
            res_list.append(multiply)
            current_number = current_number / multiply
            multiply = 1
        else:
            multiply += 1
    return res_list


def convert_fracts(lst):
    #  сначала попробуем сократить все дроби, для этого разложим на множители числители и знаменатели
    multiplier_number_list = []
    for number in lst:
        multiplier_number_list.append([devide(number[0]), devide(number[1])])
        # теперь все числа имеют вид [[1,2,3,5,5,5],[2,2,3,3,5]]
    for num in multiplier_number_list:
        for numenator in num[0]:
            current_multiplier = numenator
            if current_multiplier in num[1]:
                num[0].remove(current_multiplier)
                num[1].remove(current_multiplier)
    denominator_list = []
    for numbers_multipliers in multiplier_number_list:
        denominator_list.append(numbers_multipliers[1])  # имеем список множителей для каждого знаменателя

    """
    max_of_multippliers = max([max(i) for i in denominator_list])
    current_multiplier = 1
    while current_multiplier < max_of_multippliers:
    """

    first_denominator_multipliers = denominator_list[0]
    for multiplier in first_denominator_multipliers:
        delete = True
        for list_of_multi in denominator_list:
            if multiplier not in list_of_multi:
                delete = False
        if delete:
            for list_of_multi in denominator_list:
                list_of_multi.remove(multiplier)
    res_denominator = 0
    if denominator_list:
        for number in denominator_list:
            ready_multiplier = reduce(lambda x, y: x*y, number)
            if res_denominator == 0:
                res_denominator = ready_multiplier


