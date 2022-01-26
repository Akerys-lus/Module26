def caesarcipherchar(let, cnt):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    if let.isupper():
        let = let.lower()
        pos = alphabet.find(let)
        return alphabet[pos + cnt].upper()
    else:
        let = let.lower()
        pos = alphabet.find(let)
        return alphabet[pos + cnt]


text_file = open('text.txt', 'r')
write_file = open('cipher_text.txt', 'w')

count = 1

for i_len in text_file:
    string = ''
    for i_symb in i_len:
        if i_symb == '\n':
            break
        string = string + caesarcipherchar(i_symb, count)
    write_file.write(string + '\n')
    count += 1

text_file.close()
write_file.close()
