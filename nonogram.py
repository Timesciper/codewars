#  ссылка на кодварс
#  https://www.codewars.com/kata/5a479247e6be385a41000064/train/python

class Nonogram:

    """
    получаем на вход (((1, 1), (4,), (1, 1, 1), (3,), (1,)), ((1,), (2,), (3,), (2, 1), (4,)))
    первый тупл туплов - горизонтальная линия
    второй тупл туплов - вертикальная линия
    если 2 числа, то первое - верхнее (для горизонт)
    если 2 числа, то первое - слева (для верт)
    :return tuple of tuples like
    ((0, 0, 1, 0, 0),
    (1, 1, 0, 0, 0),
    (0, 1, 1, 1, 0),
    (1, 1, 0, 1, 0),
    (0, 1, 1, 1, 1))
    where 0 - nothing, 1 - black square
    """

    def __init__(self, clues):
        if clues:
            self.horizontal = clues[0]
            self.vertical = clues[1]

    @staticmethod
    def check_on_autoresolve(row):
        res_list = []
        for index in range(0, len(row)):
            item = row[index]
            if item == (1, 3) or item == (3, 1) or item == (5,) or item == (2, 2):
                res_list.append((item, index))
        return res_list

    def solve(self):
        res_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        locked_rows = []
        locked_columns = []
        #  проверим матрицу на изи варианты
        easy_horizontal = self.check_on_autoresolve(self.horizontal)
        easy_vertical = self.check_on_autoresolve(self.vertical)
        if easy_horizontal:
            for easy_pair in easy_horizontal:
                locked_columns.append(easy_pair[1])
                for row in res_matrix:
                    row[easy_pair[1]] = 1
                if easy_pair == (1, 3):
                    res_matrix[1][easy_pair[1]] = 0
                if easy_pair == (3, 1):
                    res_matrix[3][easy_pair[1]] = 0
                if easy_pair == (5,):
                    pass
                if easy_pair == (2, 2):
                    res_matrix[2][easy_pair[1]] = 0
        if easy_vertical:
            for easy_pair in easy_vertical:
                locked_rows.append(easy_pair[1])
                if easy_pair == (1, 3):
                    res_matrix[easy_pair[1]] = (1, 0, 1, 1, 1)
                if easy_pair == (3, 1):
                    res_matrix[easy_pair[1]] = (1, 1, 1, 0, 1)
                if easy_pair == (5,):
                    res_matrix[easy_pair[1]] = (1, 1, 1, 1, 1)
                if easy_pair == (2, 2):
                    res_matrix[easy_pair[1]] = (1, 1, 0, 1, 1)
        #  ну пошли по строкам?
        #  проверим 4ки
        solved = 0
        while solved == 0:
            print('solved')
            if len(locked_rows) == len(locked_columns) == 5:
                solved += 1
        return res_matrix
