import os


def frequency_letter(txt, freq_dct):
    for i_letter in txt:
        if i_letter not in freq_dct:
            freq_dct[i_letter] = round(txt.count(i_letter) / len(txt), 3)
    return freq_dct


frequency_dict = {}
text = open('text.txt', 'r')
new_txt = ''

for i_len in text:
    for i_symb in i_len:
        if i_symb in 'abcdefghijklmnopqrstuvwxyz':
            new_txt += i_symb

frequency_letter(new_txt, frequency_dict)

analysis_txt = open('analysis.txt', 'w')

sorted_values = sorted(frequency_dict.values())
sorted_dict = {}

for i_val in sorted_values[::-1]:
    for i_key in frequency_dict.keys():
        if frequency_dict[i_key] == i_val:
            sorted_dict[i_key] = i_val


for i_let, i_frequency in sorted_dict.items():
    string = i_let + ' ' + str(i_frequency) + '\n'
    analysis_txt.write(string)

text.close()
analysis_txt.close()
# TODO 1) не учитывается большая буква M, текст надо преобразовать к нижнему регистру - .lower()
#  2) не выполняется требование задания: "Буквы должны быть отсортированы по убыванию их доли. Буквы с равной долей
#  должны следовать в алфавитном порядке."
