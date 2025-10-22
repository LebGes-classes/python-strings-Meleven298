text = str(input())

words = []
word = ''

for symbol in text:
    if symbol == " ":
        words.append(word)
        word = ''
    else:
        word = word + symbol

words.append(word)

word_reversed = ''
words_revers = []

for word in range(len(words)-1, -1, -1):
    this_word = words[word]
    
    for symbol in this_word[::-1]:
        word_reversed = word_reversed + symbol
    
    words_revers.append(word_reversed)
    word_reversed = ''

print(words_revers)