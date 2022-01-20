def summ(*args):
    def flatten(a_list):
        result = []
        for e in a_list:
            if isinstance(e, int):
                result.append(e)
            else:
                result.extend(flatten(e))
        return result

    return sum(flatten(args))


