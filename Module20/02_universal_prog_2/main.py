def list_symbols(symb_input):
    return[i_nums for i_index, i_nums in enumerate(symb_input) if is_prime(i_nums)]


def is_prime(n):
    if n % 2 != 0 and n > 2:
        return False
    else:
        return True



