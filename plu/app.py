plural_other_than_one = [
    "af",      # Afrikaans
    "an",      # Aragonese
    "anp",     # Angika
    "as",      # Assamese
    "ast",     # Asturian
    "az",      # Azerbaijani
    "bg",      # Bulgarian
    "bn",      # Bengali
    "brx",     # Bodo
    "ca",      # Catalan
    "da",      # Danish
    "de",      # German
    "doi",     # Dogri
    "el",      # Greek
    "en",      # English
    "eo",      # Esperanto
    "es",      # Spanish
    "es_AR",   # Argentinean Spanish
    "et",      # Estonian
    "eu",      # Basque
    "ff",      # Fulah
    "fi",      # Finnish
    "fo",      # Faroese
    "fur",     # Friulian
    "fy",      # Frisian
    "gl",      # Galician
    "gu",      # Gujarati
    "ha",      # Hausa
    "he",      # Hebrew
    "hi",      # Hindi
    "hne",     # Chhattisgarhi
    "hu",      # Hungarian
    "hy",      # Armenian
    "ia",      # Interlingua
    "it",      # Italian
    "kk",      # Kazakh
    "kl",      # Greenlandic
    "kn",      # Kannada
    "ku",      # Kurdish
    "ky",      # Kyrgyz
    "lb",      # Letzeburgesch
    "mai",     # Maithili
    "ml",      # Malayalam
    "mn",      # Mongolian
    "mni",     # Manipuri
    "mr",      # Marathi
    "nah",     # Nahuatl
    "nap",     # Neapolitan
    "nb",      # Norwegian Bokmal
    "ne",      # Nepali
    "nl",      # Dutch
    "nn",      # Norwegian Nynorsk
    "no",      # Norwegian (old code)
    "nso",     # Northern Sotho
    "or",      # Oriya
    "pa",      # Punjabi
    "pap",     # Papiamento
    "pms",     # Piemontese
    "ps",      # Pashto
    "pt",      # Portuguese
    "rm",      # Romansh
    "rw",      # Kinyarwanda
    "sat",     # Santali
    "sco",     # Scots
    "sd",      # Sindhi
    "se",      # Northern Sami
    "si",      # Sinhala
    "so",      # Somali
    "son",     # Songhay
    "sq",      # Albanian
    "sv",      # Swedish
    "sw",      # Swahili
    "ta",      # Tamil
    "te",      # Telugu
    "tk",      # Turkmen
    "ur",      # Urdu
    "yo",      # Yoruba
]
plural_bigger_than_one = [
    "ach",  # Acholi
    "ak",  # Akan
    "am",  # Amharic
    "arn",  # Mapudungun
    "br",  # Breton
    "fa",  # Persian
    "fil",  # 🇵🇭 Filipino
    "fr",  # 🇫🇷 French
    "gun",  # Gun
    "ln",  # Lingala
    "mfe",  # 🇲🇺 Mauritian Creole
    "mg",  # Malagasy
    "mi",  # Maori
    "oc",  # Occitan
    "pt_BR",  # 🇧🇷 Brazilian Portuguese
    "tg",  # Tajik
    "ti",  # Tigrinya
    "tr",  # 🇹🇷 Turkish
    "uz",  # 🇺🇿 Uzbek
    "wa",  # Walloon
    # "zh",  # Chinese (debatable)
]
plural_standard_slavenic = [
    'be',  # 🇧🇾 Belarusian
    'bs',  # 🇧🇦 Bosnian
    'hr',  # 🇭🇷 Croatian
    'ru',  # 🇷🇺 Russian
    'sr',  # 🇷🇸 Serbian
    'uk',  # 🇺🇦 Ukrainian
]
plural_no_plurals = [
    'ay',	  # Aymará
    'bo',	  # Tibetan
    'cgg',	  # Chiga
    'dz',	  # Dzongkha
    'id',	  # Indonesian
    'ja',	  # Japanese
    'jbo',	  # Lojban
    'ka',	  # Georgian
    'km',	  # Khmer
    'ko',	  # Korean
    'lo',	  # Lao
    'ms',	  # Malay
    'my',	  # Burmese
    'sah',	  # Yakut
    'su',	  # Sundanese
    'th',	  # Thai
    'tt',	  # Tatar
    'ug',	  # Uyghur
    'vi',	  # Vietnamese
    'wo',	  # Wolof
    'zh',	  # Chinese [2]
]


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
flags['cz'] = ' 🇨🇿 '
flags['en'] = ' 🇬🇧 '
flags['fr'] = ' 🇫🇷 '
flags['pl'] = ' 🇵🇱 '
flags['sk'] = ' 🇸🇰 '
flags['uk'] = ' 🇺🇦 '


sample_numbers = [-5, -2, -1, 0, 1, 2, 5, 10, 12, 21, 22, 25,
                  100, 102]

# lang: str = 'cz'
# print_sample_plu(sample_numbers, apples[lang], lang, prefix=flags[lang])
# lang = 'pl'
# print_sample_plu(sample_numbers, apples[lang], lang, prefix=flags[lang])
# lang = 'uk'
# print_sample_plu(sample_numbers, apples[lang], lang, prefix=flags[lang])
# lang = 'en'
# print_sample_plu(sample_numbers, apples[lang], lang, prefix=flags[lang])
# lang = 'fr'
# print_sample_plu(sample_numbers, apples[lang], lang, prefix=flags[lang])

for lang in apples:
    print(
        flags[lang],
        ", ".join([plu(number, apples[lang], lang)
                   for number in sample_numbers])
    )
