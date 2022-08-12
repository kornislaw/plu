from lang_rules import *


def plufo(n: int, lang_code: str) -> int:
    n = abs(n)

    if lang_code in plural_bigger_than_one:  # i.e. 🇫🇷
        return [0, 1][n > 1]
    elif lang_code in plural_other_than_one:  # i.e. 🇬🇧
        return [0, 1][n != 1]
    elif lang_code in plural_no_plurals:  # i.e. 🇹🇼
        return 0
    elif lang_code in ['cz', 'sk']:  # 🇨🇿 🇸🇰
        return [[2, 1][n >= 2 and n <= 4], 0][n == 1]
    elif lang_code == "pl":  # 🇵🇱
        return [[2, 1][n % 10 >= 2 and n % 10 <= 4 and (
                n % 100 < 10 or n % 100 >= 20)], 0][n == 1]
    elif lang_code in plural_standard_slavenic:  # i.e. 🇺🇦
        return [[2, 1][n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20)], 0][n % 10 == 1 and n % 100 != 11]
    elif lang_code == 'jv':  # Javanese
        return [0, 1][n != 0]


def plu(number: int, forms_array: list[str], lang_code: str) -> str:
    return f"{number} {forms_array[plufo(number, lang_code)]}"


def get_sample_plu(
        numbers: list[int],
        forms: list[str],
        lang_code: str,
        prefix: str = '',
        suffix: str = '') -> None:

    return [plu(number, forms, lang_code) for number in numbers]


apples: dict = {}
apples['cz'] = ['jablko', 'jablka', 'jablek']
apples['en'] = ['apple', 'apples']
apples['fr'] = ['pomme', 'pommes']
apples['pl'] = ['jabłko', 'jabłka', 'jabłek']
apples['sk'] = ['jablko', 'jablka', 'jablek']
apples['uk'] = ['яблуко', 'яблука', 'яблук']

flags: dict = {}
flags['cz'] = '🇨🇿 cz'
flags['en'] = '🇬🇧 en'
flags['fr'] = '🇫🇷 fr'
flags['pl'] = '🇵🇱 pl'
flags['sk'] = '🇸🇰 sk'
flags['uk'] = '🇺🇦 uk'


sample_numbers = [-5, -2, -1, 0, 1, 2, 5, 10, 12, 21, 22, 25,
                  100, 102]


for lang in apples:
    print(
        flags[lang],
        ", ".join([plu(number, apples[lang], lang)
                   for number in sample_numbers])
    )
