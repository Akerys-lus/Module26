## Задача 1. Информация о системе
Чтобы преподавателям было проще помогать вам при возникновении различных ошибок, нужно собрать информацию об операционной системе и версии пайтона. Для этого запустите код ниже из файла main.py. 

````python
import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname('windows'),
    sys.version('10, для образовательных учреждений'),
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
````