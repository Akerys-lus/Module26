def sort_tpl(lst):
    flag = True
    for i in lst:
        if type(i) != int:
            flag = False

    if flag:
        lst = tuple(sorted(lst))
    else:  # TODO вся эта ветка else не нужна, если её убрать, список всё равно вернётся следующей командой после
           #  условного оператора
        return lst
    return lst
