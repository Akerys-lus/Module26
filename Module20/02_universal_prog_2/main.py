def list_symbols(symb_input):
    return[i_nums for i_index, i_nums in enumerate(symb_input) if is_prime(i_nums)]


def is_prime(n):
    if n % 2 != 0 and n > 2:
        return False  # TODO просто верните инвертированный (not) результат сравнения
    else:
        return True


for i in range(20):
    print(f'{i} - {is_prime(i)}')

# TODO функция определения простоты числа не верна:
# 0 - True   не простое число на самом деле
# 1 - True   аналогично
# 2 - True   ок
# 3 - False  это простое!
# 4 - True   не простое!
# 5 - False  это простое!
