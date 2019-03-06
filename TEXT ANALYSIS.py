import pymorphy2
import sys
import re


def text_analysis():
    print('Введите текст:')
    print('Для окончания ввода нажмите CTRL + D')
    analysis = pymorphy2.MorphAnalyzer()
    source_text = list(map(str.strip, sys.stdin))
    slightly_modified_text = list()
    for proposals in source_text:
        slightly_modified_text.append(proposals.split('.'))
    new_slightly_modified_text = list()
    for sublist in slightly_modified_text:
        split_sentences1 = list()
        for sentences in sublist:
            text = re.sub(r'[^\w\s]', ' ', sentences)
            split_sentences1.append(text.split())
        new_slightly_modified_text.append(split_sentences1)
    selected_text = list()
    color = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый', 'белый', 'черный',
             'розовый']
    for sublist in new_slightly_modified_text:
        for sentences in sublist:
            split_sentences2 = list()
            for q in sentences:
                check = analysis.tag(q.strip())[0].cyr_repr
                if check[0:3] == 'СУЩ':
                    check_v2 = analysis.parse(q)[0].normal_form
                    if check_v2 == 'еда':
                        pass
                    else:
                        split_sentences2.append(check_v2)
                elif check[0:4] == 'ПРИЛ':
                    check_v2 = analysis.parse(q)[0].normal_form
                    if check_v2 in color:
                        split_sentences2.append(check_v2)
                    else:
                        pass
            if not split_sentences2:
                pass
            else:
                selected_text.append(split_sentences2)
    return selected_text


new_list = text_analysis()
print(new_list)
