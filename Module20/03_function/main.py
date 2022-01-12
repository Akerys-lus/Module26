def slicer(i_tuple, element):
    if element in i_tuple:
        if i_tuple.count(element) > 1:
            first_index = i_tuple.index(element)
            second_index = i_tuple.index(element, first_index + 1) + 1
            return i_tuple[first_index:second_index]
        else:
            return i_tuple[any_tuple.index(element):]  # TODO содержит опечатку
    else:
        return ()


print(slicer([2, 3, 4, 2, 1, 3, 5], 21))

