import json
import os
from pprint import pprint
import chardet


def read_news_file_json(file_name):
    with open(file_name, "rb") as cb_file:
        data = cb_file.read()
        encoding = chardet.detect(data)
        s = data.decode(encoding['encoding'])
        return json.loads(s)


def string_stats(string, stat):
    for word in string.split(" "):
        if len(word) >= 6:
            word = word.lower()
            if word in stat:
                stat[word] += 1
            else:
                stat[word] = 1


def count_words(news):
    words_stat = {}
    for item in news["rss"]["channel"]["items"]:
        description = item["description"]
        title = item["title"]
        string_stats(description, words_stat)
        string_stats(title, words_stat)
    return words_stat


def top_10(stat):
    s = sorted(stat.items(), key=lambda x: x[1], reverse=True)
    return s[:10]


def get_json_files(dir_path):
    return [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.splitext(f)[1] == ".json"]


if __name__ == "__main__":
    for path in get_json_files("."):
        news = read_news_file_json(path)
        stat = count_words(news)
        print(path)
        pprint(top_10(stat))
        print()
