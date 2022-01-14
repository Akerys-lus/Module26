def sort_tpl(lst):
    flag = True
    for i in lst:
        if type(i) != int:
            flag = False

    if flag:
        lst = tuple(sorted(lst))

    return lst
