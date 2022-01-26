sum_num = []
numbers = open('numbers.txt', 'r')
for i_symb in numbers:
    for i_numb in i_symb:
        if i_numb.isnumeric():
            sum_num.append(int(i_numb))

numbers.close()

sum_num = sum(sum_num)
answer_res = open('answer.txt', 'w')
answer_res.write(str(sum_num))

answer_res.close()
