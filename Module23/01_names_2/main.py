file_txt = open('people.txt', 'r', encoding="utf8")
sum_symb = 0
count_len = 0

for i_len in file_txt:
    count_len += 1
    count_symb_len = 0
    try:
        count_symb_len = len(i_len.strip())
        if count_symb_len < 3:
            raise ValueError
        sum_symb += count_symb_len
    except ValueError:
        print('В {} строке меньше трёх символов.'.format(count_len))

print('Общее кол-во символов: ', sum_symb)

