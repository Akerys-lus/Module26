def sequence_numb(num, count):
    numb = num - (num - count)
    count += 1
    print(count)
    if count < num:
        sequence_numb(num, count)


number = int(input('Введите num: '))
count_sequence = 0
sequence_numb(number, count_sequence)

