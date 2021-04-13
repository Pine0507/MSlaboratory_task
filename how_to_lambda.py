# any_sort.pyで昇順降順に関するラムダ式を作ったためこちらで 偶昇順 , 奇昇順　の並び方をラムダで実現
import any_sort


def main():
    """
    >>> main()
    selection_sort
    5
    [1, 4, 5, 7, 8, 9, 9, 111]
    4 8 1 5 7 9 9 111 
    """

    sort_list = [111, 4, 9, 1, 8, 7, 5, 9]
    num = len(sort_list)
    any_sort.list_selection_sort(sort_list, num, lambda x, y: x < y)
    print(sort_list)

    map_even = map(lambda x: print(x, end=" ") if x %
                   2 == 0 else "karioki", sort_list)
    map_odd = map(lambda x: print(x, end=" ") if x %
                  2 == 1 else "karioki", sort_list)

    list(map_even)
    list(map_odd)

    return


if __name__ == '__main__':
    import doctest
    doctest.testmod()
