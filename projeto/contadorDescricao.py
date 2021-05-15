import jsonlines
import json
import codecs


def word_count(str, dic):
    counts = dic
    if str is None: 
        return counts
    words = str.split()
    if counts is None:
        counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


dic = dict()
with open('final-3.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    for line in data:
        #print(dic)
        #print(line['titulo'])
        dic = word_count(line['nome da vaga'], dic)
    
ordered = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
with open('countNomeVaga.json', 'w', encoding='utf8') as json_file:
    json.dump(ordered, json_file, ensure_ascii=False)
