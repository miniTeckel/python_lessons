import requests

API_KEY = 'trnsl.1.1.20171009T193951Z.9a70b26a8fb1a044.df3b963deb27ef7eb05910a8b49be1823466759c'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


def translate(source_path, result_path, from_lang, to_lang="ru"):
    with open(source_path, "rt") as source:
        text = translate_it(source.read(), from_lang, to_lang)
        with open(result_path, "wt") as result:
            result.write(text)


FILES_TO_TRANSLATE = [
    {"from": "DE.txt", "to": "DE_RU.txt", "lang": "de"},
    {"from": "ES.txt", "to": "ES_RU.txt", "lang": "es"},
    {"from": "FR.txt", "to": "FR_RU.txt", "lang": "fr"},
]


if __name__ == "__main__":
    for t in FILES_TO_TRANSLATE: 
        translate(t["from"], t["to"], t["lang"])
