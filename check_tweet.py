"""
https://www.codewars.com/kata/59922ce23bfe2c10d7000057/train/python
FIRE = you are fired
FURY - i am furious
если подряд - то в первое добавляется and you
во втором - really
если нет совпадений - то Fake tweet.
(E,F,I,R,U,Y)
"""
import re


def check_for_symbols(a:str):
    """
    Проверим строку на наличие символов, кроме (E,F,I,R,U,Y)
    """
    available_letters = ("E", "F", "I", "R", "U", "Y")
    a = set(a)
    for item in a:
        if item not in available_letters:
            return False
    return True


def fire_and_fury(tweet):
    if not check_for_symbols(tweet):
        return "Fake tweet."
    if len(tweet) < 4:
        return "Fake tweet."
    # теперь надо идти по строке и собирать слова
    # если находим одно из двух слов - увеличиваем счетчик, как только слово меняется
    # - записываем в строку и обеуляем счетчик
    sub_fury = 'FURY'
    sub_fire = 'FIRE'
    result_fury = [_.start() for _ in re.finditer(sub_fury, tweet)]  # находит все FURY в строке
    result_fire = [_.start() for _ in re.finditer(sub_fire, tweet)]  # находит все FIRE в строке
    # теперь нужно составить сиквенсы и сформировать конечную строку
    res_keywords_indexes_list = result_fury + result_fire
    res_keywords_indexes_list = sorted(res_keywords_indexes_list)
    counter = 0
    word = ''
    res_list_of_sequences = []
    # проверим нашли в принципе что-то или нет
    if not res_keywords_indexes_list:
        return 'Fake tweet.'

    for index_of_keyword in res_keywords_indexes_list:
        if not word:
            if index_of_keyword in result_fire:
                word = "FIRE"
                counter += 1
            else:
                word = "FURY"
                counter += 1
        else:
            if word == 'FIRE':
                if index_of_keyword in result_fire:
                    counter += 1
                else:
                    res_list_of_sequences.append(('FIRE', counter))
                    word = 'FURY'
                    counter = 1
            else:
                if index_of_keyword in result_fury:
                    counter += 1
                else:
                    res_list_of_sequences.append(('FURY', counter))
                    word = 'FIRE'
                    counter = 1
    res_list_of_sequences.append((word, counter))
    res_string = ""
    for item in res_list_of_sequences:
        addon = ""
        if item[0] == 'FIRE':
            if item[1] > 1:
                addon = 'and you '*(item[1]-1)
            res_string += ' You {}are fired!'.format(addon)
        else:
            if item[1] > 1:
                addon = "really "*(item[1]-1)
            res_string += " I am {}furious.".format(addon)
    return res_string[1:]
