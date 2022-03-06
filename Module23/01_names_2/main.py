file_txt = open('people.txt', 'r', encoding="utf8")
sum_symb = 0
count_len = 0

for i_len in file_txt:
    count_len += 1
    count_symb_len = 0
    for i_symb in i_len:
        if i_symb.isalpha():
            count_symb_len += 1
    try:
        if count_symb_len > 4:
            sum_symb += count_symb_len
        else:
            sum_symb += count_symb_len
            raise ValueError
    except ValueError:
        print('В {} строке меньше трёх символов.'.format(count_len))

print('Общее кол-во символов: ', sum_symb)
