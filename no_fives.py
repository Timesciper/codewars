"""
https://www.codewars.com/kata/5813d19765d81c592200001a/train/python
вернуть сколько чисел из промежутка не имеют число цифру 5 в себе
первое число всеггда меньше второго, могут быть отрицательные промежутки
"""


def dont_give_me_five(start, end):
    return len([x for x in range(start, end+1) if "5" not in list(str(x))])
