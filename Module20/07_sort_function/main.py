def sort_tpl(lst):
    flag = True
    for i in lst:
        if float(i) != int(i):  # TODO на самом деле надо проверить только тип if type(i) != int:
            flag = False

    if flag:
        lst = tuple(sorted(lst))
        return lst  # TODO вынесите эту строку из условного оператора чтобы она
    else:
        return lst


print(sort_tpl([.1, -1, 0, ]))
