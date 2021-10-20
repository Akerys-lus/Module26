word = input('Введите слово: ')
word_reverse = ''
for i in word:
    word_reverse = i + word_reverse
if word == word_reverse:
    print('Слово является палиндромом.')
else:
    print('Слово не является палиндромом.')
