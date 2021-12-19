count_word = int(input('Введите количество пар слов: '))
dict_words = {}
for i in range(1, count_word + 1):
    (first_word, second_word) = input('{} пара: '.format(i)).split(' - ')
    dict_words[first_word] = second_word
    dict_words[second_word] = first_word

while True:
    new_word = input('Введите слово: ')
    if new_word in dict_words.keys():
        print('Синоним: ', dict_words[new_word])
        break
    else:
        print('Такого слова в словаре нет.')
