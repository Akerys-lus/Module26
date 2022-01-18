def calculating_math_func(data, fact={0: 1}):
    if data not in fact:
        num = max(fact)
        for i_num in range(num + 1, data + 1):
            fact[i_num] = fact[i_num - 1] * i_num
    fact[data] = (fact[data] / data ** 3) ** 10
    print(fact[data])

