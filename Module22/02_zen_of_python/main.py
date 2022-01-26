text = open('zen.txt', 'r')
new_txt = []
flag = True
for i_len in text:
    new_txt.append(i_len)
for i_rev_len in new_txt[::-1]:
    if flag:
        print(i_rev_len + '\n', end='')
        flag = False
    else:
        print(i_rev_len, end='')


text.close()
