import nltk
import pymorphy2
nltk.download('punkt')

# TODO (sirotkin.nikola@mail.ru): перед запуском необходимо установть библиотеки: nltk и pymorphy2

prob_thresh = 0.4

morph = pymorphy2.MorphAnalyzer()
name_list = []
with open('text.txt', 'r', encoding='Utf8') as text:
    new_text = text.read()
    for word in nltk.word_tokenize(new_text):
        for p in morph.parse(word):
            if 'Name' in p.tag and p.score >= prob_thresh:
                if p.normal_form.title() not in name_list:
                    name_list.append(p.normal_form.title())
print('Найденные имена в тексте: ')
for result_name in name_list:
    print(result_name)