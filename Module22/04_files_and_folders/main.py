import os


def file_sizes(path_fl):
    files_stat = [0, 0, 0]

    for i_elem in os.listdir(path_fl):
        if os.path.isfile(os.path.abspath(os.path.join(path_fl, i_elem))):
            file_path = os.path.abspath(os.path.join(path_fl, i_elem))
            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size
            files_stat[1] += 1

        else:
            results = file_sizes(os.path.abspath(os.path.join(path_fl, i_elem)))
            files_stat[0] += results[0]
            files_stat[1] += results[1]
            files_stat[2] += 1
    return files_stat


name_files = input('Введите название файла: ')
path = os.path.abspath(os.path.join('..', '..', name_files))


results = file_sizes(path)
print('Размер каталога (в Кб):', results[0] / 1024)
print('Количество подкаталогов:', results[2])
print('Количество файлов:', results[1])
