import os


def save_files(string):
    way = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ')
    r_path = way.replace(" ", "/")
    real_path = str('C:/') + str(os.path.join(r_path))
    if os.path.exists(real_path):
        filename = input('Введите имя файла: ')
        path = real_path + filename
        check_file = os.path.exists(path)
        if check_file:
            print('Файл с таким именем уже существует!')
            ans = input('Вы действительно хотите перезаписать файл? ').lower()
            if ans == 'да' or ans == 'yes':
                file = open(path, 'w')
                file.write(string)
                file.close()
                print('Файл успешно перезаписан!')
            else:
                print('Файл не перезаписан')
        else:
            file = open(path, 'w')
            file.write(string)
            file.close()
            print('Файл успешно сохранён!')
    else:
        print('Такой директории нет')


text = input('Введите строку: ')

save_files(text)
