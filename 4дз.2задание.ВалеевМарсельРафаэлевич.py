import re

text = input()

words = []
word = ''
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for symbol in text:
    if symbol in letters:
        word = word + symbol
        if len(word) > 19:
            words.append(word)
            word = ''
    else:
        words.append(word)
        word = ''
        
if word:
    words.append(word)

sypher_text = ''

K = len(max(words, key=len))


for letter in text:
    sypher_text_length = len(sypher_text)
    
    for i in range(len(letters)):
        if letter == letters[i] and letter != "" and sypher_text_length == len(sypher_text):
            letter = letters[(i+K)%52]
            sypher_text += letter
    if letter == " ":
        sypher_text += letter
        
print(sypher_text)