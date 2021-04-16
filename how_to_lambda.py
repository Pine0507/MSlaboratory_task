def sort(values, comp_func):
    """
    昇順
    comp_func = lambda a, b: a if a<b else b

    降順
    comp_func = lambda a, b: a if a>b else b

    偶数昇順、奇数昇順
    comp_func = lambda a, b: a if \
                            a % 2 == 0 and b % 2 == 1 else \
                            (b if b%2==0 and a%2==1 else (a if a<b else b))
    """

    """
    以下doctest
    >>> values = [111, 4, 9, 1, 8, 7, 5, 9]
    >>> sort(values,comp_func = lambda a, b: a if a<b else b)
    [1, 4, 5, 7, 8, 9, 9, 111]

    >>> values = [111, 4, 9, 1, 8, 7, 5, 9]
    >>> sort(values,comp_func = lambda a, b: a if a>b else b)
    [111, 9, 9, 8, 7, 5, 4, 1]

    >>> values = [111, 4, 9, 1, 8, 7, 5, 9]
    >>> sort(values,comp_func = lambda a, b: a if \
                            a % 2 == 0 and b % 2 == 1 else \
                            (b if b%2==0 and a%2==1 else (a if a<b else b)))
    [4, 8, 1, 5, 7, 9, 9, 111]
    """
    num = len(values)
    for i in range(0, num):
        tmp_value = values[i]
        tmp_index = i
        for j in range(i, num):
            if tmp_value != comp_func(values[j], tmp_value):
                tmp_index = j
            tmp_value = comp_func(values[j], tmp_value)
        values[tmp_index] = values[i]
        values[i] = tmp_value
        """
        values.remove(tmp_value)
        values.insert(0, tmp_value)
        new_list.insert(0, tmp_value)
        """
    print(values)

    return


if __name__ == '__main__':
    import doctest
    doctest.testmod()
