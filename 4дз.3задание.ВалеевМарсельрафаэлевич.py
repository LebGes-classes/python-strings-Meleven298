import re

text = input()

words_dictionary = {}
lower_text = ''
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
bukvi = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

for letter in text:
    for i in range(26, len(bukvi)):
        if i < 52 and letter == letters[i]:
            letter = letters[i-26]
        if letter == bukvi[i] and i > 32:
            letter = bukvi[i-33]
    lower_text += letter

words = re.findall(r'[a-zа-я]+', lower_text)

for word in words:
    if word not in words_dictionary:
        words_dictionary[word] = 1
    else:
        words_dictionary[word] += 1

words_copy = dict(words_dictionary)
all_words = []

while words_dictionary:
    max_word = max(words_dictionary, key=words_dictionary.get)
    all_words.append(max_word)
    
    del words_dictionary[max_word]

for i in range(1, 6):
    words_place = str(i) + '.' + ' ' + all_words[i-1] + ':' + ' ' + str(words_copy[all_words[i-1]])

    print(words_place)