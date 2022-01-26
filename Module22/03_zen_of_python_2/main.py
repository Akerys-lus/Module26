import os


path_file = os.path.abspath('../02_zen_of_python/zen.txt')
text = open(path_file, 'r')
len_cnt = 0
word_cnt = 0
symb_cnt = 0
rare_symb = ''
all_letters = ''
prev_let = 'a'
for i_len in text:
    len_cnt += 1
    for i_symb in i_len:

        if i_symb == ' ':
            word_cnt += 1
        if i_symb not in " '.,!-*":
            symb_cnt += 1
            all_letters += i_symb

text.close()

for i_letter in all_letters:
    if all_letters.count(i_letter.lower()) < all_letters.count(prev_let.lower()):
        rare_symb = i_letter
        prev_let = i_letter

word_cnt += len_cnt

print('Количество букв в файле:', symb_cnt)
print('Количество слов в файле:', word_cnt)
print('Количество строк в файле:', len_cnt)
print('Наиболее редкая буква:', rare_symb)
