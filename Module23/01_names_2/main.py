file_txt = open('people.txt', 'r', encoding="utf8")
sum_symb = 0
count_len = 0

for i_len in file_txt:
    count_len += 1
    count_symb_len = 0
    for i_symb in i_len:  # TODO количество знаков в имени считайте с помощью len(), но перед этим выполните strip()
                          #  чтобы убрать символы форматирования
        if i_symb.isalpha():
            count_symb_len += 1
    try:
        if count_symb_len > 4:
            # TODO Сравнение должно быть такое: if count_symb_len < 3: это логичино и точнее, чем сейчас - отбираются
            #  имена из 4х буквы бракуются, а должны "браковаться" только имена длиной 0, 1 и 2 символа, из трех букв
            #  уже "хорошо", согласно заданию
            sum_symb += count_symb_len  # TODO Эта строка кода дублируется в обоих ветках условного оператора и должна
                                        #  выполняться безусловно
        else:
            sum_symb += count_symb_len
            raise ValueError
    except ValueError:
        print('В {} строке меньше трёх символов.'.format(count_len))

print('Общее кол-во символов: ', sum_symb)

