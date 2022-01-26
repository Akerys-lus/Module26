import os
import zipfile


def frequency_letter(txt, freq_dct):
    for i_letter in txt:
        if i_letter not in freq_dct:
            freq_dct[i_letter] = round(txt.count(i_letter) / len(txt), 6)
    return freq_dct


zip_archive = zipfile.ZipFile('voyna-i-mir.zip', 'r')
ext_zip = zip_archive.extract('voyna-i-mir.txt')

open_zip = open('voyna-i-mir.txt', 'r', encoding="utf8")

frequency_dict = {}
new_txt = ''

for i_len in open_zip:
    for i_symb in i_len:
        if i_symb.lower() in 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            new_txt += i_symb

frequency_letter(new_txt, frequency_dict)

sorted_values = sorted(frequency_dict.values())
sorted_dict = {}

for i_val in sorted_values[::-1]:
    for i_key in frequency_dict.keys():
        if frequency_dict[i_key] == i_val:
            sorted_dict[i_key] = i_val

for i_let, i_frequency in sorted_dict.items():
    print(i_let, ':', i_frequency)

open_zip.close()
zip_archive.close()
