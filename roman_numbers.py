"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

"""


class RomanNumerals:
    def to_roman(self, val: int) -> str:
        m = ["", "M", "MM", "MMM", "MMMM", "MMMMM", 'MMMMMM', "MMMMMMM", "MMMMMMMM", "MMMMMMMMM"]
        c = ["", "C", "CC", "CCC", "CD", "D",
             "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L",
             "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V",
             "VI", "VII", "VIII", "IX"]
        thousands = m[val // 1000]
        hundreds = c[(val % 1000) // 1000]
        tens = x[(val % 1000) // 100]
        ones = i[(val % 100) % 10]
        return ''.join([thousands, hundreds, tens, ones])

    def from_roman(self, roman_num: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i + 2] in roman:
                num += roman[roman_num[i:i + 2]]
                i += 2
            else:
                num += roman[roman_num[i]]
                i += 1
        return num
