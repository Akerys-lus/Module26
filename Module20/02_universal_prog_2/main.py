def list_symbols(symb_input):
    return [i_nums for i_index, i_nums in enumerate(symb_input) if is_prime(i_nums)]


def is_prime(n):
    for i_numb in range(2, n):
        if n % i_numb == 0:
            return False
    return True
