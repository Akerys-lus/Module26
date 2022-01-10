def sort_tpl(lst):
    flag = True
    for i in lst:
        if float(i) != int(i):
            flag = False

    if flag:
        lst = tuple(sorted(lst))
        return lst
    else:
        return lst

