import os


def file_sizes(pth):
    files_stat = [0, 0, 0]

    for i_elem in os.listdir(pth):
        if os.path.isfile(os.path.abspath(os.path.join(pth, i_elem))):
            file_path = os.path.abspath(os.path.join(pth, i_elem))
            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size
            files_stat[1] += 1

        else:
            files_stat[0] += (file_sizes(os.path.abspath(os.path.join(pth, i_elem))))[0]
            files_stat[1] += (file_sizes(os.path.abspath(os.path.join(pth, i_elem))))[1]
            files_stat[2] += 1
    return files_stat


name_files = input('Введите название файла: ')
path = os.path.abspath(os.path.join('..', '..', name_files))

print('Размер каталога (в Кб):', file_sizes(path)[0] / 1024)
print('Количество файлов:', file_sizes(path)[1])
print('Количество подкаталогов:', file_sizes(path)[2])
