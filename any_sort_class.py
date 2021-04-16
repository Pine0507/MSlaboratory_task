import double_list
import copy
import sys


class AbstractSort:
    def sort(self, values_list, num, comp_func):
        raise NotImplementedError


class Insert_sort(AbstractSort):
    def sort(self, values_list, num, comp_func):
        print("insert_sort")
        for i in range(1, num):
            tmp = values_list[i]
            j = i-1
            while j >= 0 and comp_func(values_list[j], tmp):
                values_list[j+1] = values_list[j]
                j = j-1
            values_list[j+1] = tmp
            print(values_list)

        return


class Bubble_sort(AbstractSort):
    def sort(self, values_list, num, comp_func):
        print("bubble_sort")
        flag = 1
        exchange_count = 0
        while flag == 1:
            flag = 0
            for j in range(num-1, 0, -1):
                if comp_func(values_list[j], values_list[j-1]):
                    tmp = values_list[j]
                    values_list[j] = values_list[j-1]
                    values_list[j-1] = tmp
                    flag = 1
                    exchange_count += 1
                    print(values_list)

        print(exchange_count)
        return


class Selection_sort(AbstractSort):
    def sort(self, values_list, num, comp_func):
        print("selection_sort")

        exchange_count = 0
        exchange_flag = 0
        for i in range(num):
            minj = i
            for j in range(i, num, 1):
                if comp_func(values_list[j], values_list[minj]):
                    minj = j
                    exchange_flag = 1
            tmp = values_list[i]
            values_list[i] = values_list[minj]
            values_list[minj] = tmp
            if exchange_flag:
                exchange_count += 1
                print(values_list)
            exchange_flag = 0
        print(exchange_count)
        return


class Double_insert(AbstractSort):
    def sort(self, values_list, num, comp_func):
        print("insert_sort by double_list")

        sort_list = double_list.Double_List()

        for i in range(num-1, -1, -1):
            sort_list.insert(values_list[i])

        sort_list.all_node_show()

        tmp_node = sort_list.head_node

        for i in range(1, num, 1):
            tmp_node = tmp_node.next
            tmp_j_node = tmp_node.prev
            tmp_value = tmp_node.value
            j = i-1
            while j >= 0 and comp_func(tmp_j_node.value, tmp_value):
                tmp_j_node.next.value = tmp_j_node.value
                tmp_j_node = tmp_j_node.prev
                j = j-1
            tmp_j_node.next.value = tmp_value
            sort_list.all_node_show()

        return


class Double_bubble(AbstractSort):
    def sort(self, values_list, num, comp_func):
        print("bubble_sort by double_list")

        sort_list = double_list.Double_List()

        for i in range(num-1, -1, -1):
            sort_list.insert(values_list[i])

        tmp_node = sort_list.head_node.prev

        flag = 1
        exchange_count = 0

        tmp_node = tmp_node.prev

        while flag:
            flag = 0
            for j in range(num):
                if comp_func(tmp_node.value, tmp_node.prev.value) and \
                        tmp_node != sort_list.head_node:

                    tmp_value = tmp_node.value
                    tmp_node.value = tmp_node.prev.value
                    tmp_node.prev.value = tmp_value
                    flag = 1
                    exchange_count += 1
                tmp_node = tmp_node.prev
        sort_list.all_node_show()
        print(exchange_count)

        return


class Double_selection(AbstractSort):
    def sort(self, values_list, num, comp_func):
        print("selection_sort by double_list")

        sort_list = double_list.Double_List()

        for i in range(num-1, -1, -1):
            sort_list.insert(values_list[i])
        print(values_list)

        tmp_node = sort_list.head_node
        j_tmp_node = tmp_node

        exchange_count = 0
        exchange_flag = 0

        for i in range(0, num):
            biggest_value = tmp_node.value
            exchange_node = double_list.Node(None)

            for j in range(i, num):

                if comp_func(j_tmp_node.value, biggest_value):
                    biggest_value = j_tmp_node.value
                    exchange_node = j_tmp_node
                    exchange_flag = 1
                j_tmp_node = j_tmp_node.next

            # 交換部分で素直にノードごと入れ替えた
            # 今までの最大値探索、削除、挿入では重複する要素が存在する場合対応できなかった
            exchange_node.value = tmp_node.value
            tmp_node.value = biggest_value

            """
            sort_list.delete(biggest_value)
            for i in range(same_num_count):
                sort_list.insert(biggest_value)
            """

            if exchange_flag:
                exchange_count += 1
            else:
                pass
            tmp_node = tmp_node.next
            j_tmp_node = tmp_node
            exchange_flag = 0

        sort_list.all_node_show()
        print(exchange_count)

        return


def get_sort_instance(algorithm_name):
    if algorithm_name == "insert_sort":
        return Insert_sort()
    elif algorithm_name == "bubble_sort":
        return Bubble_sort()
    elif algorithm_name == "selection_sort":
        return Selection_sort()
    elif algorithm_name == "double_insert":
        return Double_insert()
    elif algorithm_name == "double_bubble":
        return Double_bubble()
    elif algorithm_name == "double_selection":
        return Double_selection()
    else:
        print("Error! Do not conduct any methods.")
        print("Please cheak the spell you typed.")
        sys.exit(1)


def main():
    """
    >>> values = [10,5,7,8,8,20,100,1]
    >>> num = len(values)

    >>> values_tmp = copy.copy(values)
    >>> _c = Bubble_sort()
    >>> _c.sort(values_tmp, num ,lambda x, y: x < y)
    bubble_sort
    [10, 5, 7, 8, 8, 20, 1, 100]
    [10, 5, 7, 8, 8, 1, 20, 100]
    [10, 5, 7, 8, 1, 8, 20, 100]
    [10, 5, 7, 1, 8, 8, 20, 100]
    [10, 5, 1, 7, 8, 8, 20, 100]
    [10, 1, 5, 7, 8, 8, 20, 100]
    [1, 10, 5, 7, 8, 8, 20, 100]
    [1, 5, 10, 7, 8, 8, 20, 100]
    [1, 5, 7, 10, 8, 8, 20, 100]
    [1, 5, 7, 8, 10, 8, 20, 100]
    [1, 5, 7, 8, 8, 10, 20, 100]
    11

    >>> values_tmp = copy.copy(values)
    >>> _c = Insert_sort()
    >>> _c.sort(values_tmp, num ,lambda x, y: x > y)
    insert_sort
    [5, 10, 7, 8, 8, 20, 100, 1]
    [5, 7, 10, 8, 8, 20, 100, 1]
    [5, 7, 8, 10, 8, 20, 100, 1]
    [5, 7, 8, 8, 10, 20, 100, 1]
    [5, 7, 8, 8, 10, 20, 100, 1]
    [5, 7, 8, 8, 10, 20, 100, 1]
    [1, 5, 7, 8, 8, 10, 20, 100]

    >>> values_tmp = copy.copy(values)
    >>> _c = Selection_sort()
    >>> _c.sort(values_tmp, num ,lambda x, y: x < y)
    selection_sort
    [1, 5, 7, 8, 8, 20, 100, 10]
    [1, 5, 7, 8, 8, 10, 100, 20]
    [1, 5, 7, 8, 8, 10, 20, 100]
    3

    >>> values_tmp = copy.copy(values)
    >>> _c = Double_bubble()
    >>> _c.sort(values_tmp, num ,lambda x, y: x < y)
    bubble_sort by double_list
    1 5 7 8 8 10 20 100
    11

    >>> values_tmp = copy.copy(values)
    >>> _c = Double_insert()
    >>> _c.sort(values_tmp, num ,lambda x, y: x > y)
    insert_sort by double_list
    10 5 7 8 8 20 100 1
    5 10 7 8 8 20 100 1
    5 7 10 8 8 20 100 1
    5 7 8 10 8 20 100 1
    5 7 8 8 10 20 100 1
    5 7 8 8 10 20 100 1
    5 7 8 8 10 20 100 1
    1 5 7 8 8 10 20 100

    >>> values_tmp = copy.copy(values)
    >>> _c = Double_selection()
    >>> _c.sort(values_tmp, num ,lambda x, y: x < y)
    selection_sort by double_list
    [10, 5, 7, 8, 8, 20, 100, 1]
    1 5 7 8 8 10 20 100
    3

    ここまでで課題6前半
    以後factory_method実行例

    >>> values = [10,5,7,8,8,20,100,1]
    >>> num = len(values)


    >>> sort_arg = "bubble_sort"

    >>> values_tmp = copy.copy(values)
    >>> _c = get_sort_instance(sort_arg)
    >>> _c.sort(values_tmp, num ,lambda x, y: x < y)
    bubble_sort
    [10, 5, 7, 8, 8, 20, 1, 100]
    [10, 5, 7, 8, 8, 1, 20, 100]
    [10, 5, 7, 8, 1, 8, 20, 100]
    [10, 5, 7, 1, 8, 8, 20, 100]
    [10, 5, 1, 7, 8, 8, 20, 100]
    [10, 1, 5, 7, 8, 8, 20, 100]
    [1, 10, 5, 7, 8, 8, 20, 100]
    [1, 5, 10, 7, 8, 8, 20, 100]
    [1, 5, 7, 10, 8, 8, 20, 100]
    [1, 5, 7, 8, 10, 8, 20, 100]
    [1, 5, 7, 8, 8, 10, 20, 100]
    11


    >>> sort_arg = "insert_sort"

    >>> values_tmp = copy.copy(values)
    >>> _c = get_sort_instance(sort_arg)
    >>> _c.sort(values_tmp, num ,lambda x, y: x > y)
    insert_sort
    [5, 10, 7, 8, 8, 20, 100, 1]
    [5, 7, 10, 8, 8, 20, 100, 1]
    [5, 7, 8, 10, 8, 20, 100, 1]
    [5, 7, 8, 8, 10, 20, 100, 1]
    [5, 7, 8, 8, 10, 20, 100, 1]
    [5, 7, 8, 8, 10, 20, 100, 1]
    [1, 5, 7, 8, 8, 10, 20, 100]


    >>> sort_arg = "selection_sort"

    >>> values_tmp = copy.copy(values)
    >>> _c = get_sort_instance(sort_arg)
    >>> _c.sort(values_tmp, num ,lambda x, y: x < y)
    selection_sort
    [1, 5, 7, 8, 8, 20, 100, 10]
    [1, 5, 7, 8, 8, 10, 100, 20]
    [1, 5, 7, 8, 8, 10, 20, 100]
    3


    >>> sort_arg = "double_bubble"

    >>> values_tmp = copy.copy(values)
    >>> _c = get_sort_instance(sort_arg)
    >>> _c.sort(values_tmp, num ,lambda x, y: x < y)
    bubble_sort by double_list
    1 5 7 8 8 10 20 100
    11


    >>> sort_arg = "double_insert"

    >>> values_tmp = copy.copy(values)
    >>> _c = get_sort_instance(sort_arg)
    >>> _c.sort(values_tmp, num ,lambda x, y: x > y)
    insert_sort by double_list
    10 5 7 8 8 20 100 1
    5 10 7 8 8 20 100 1
    5 7 10 8 8 20 100 1
    5 7 8 10 8 20 100 1
    5 7 8 8 10 20 100 1
    5 7 8 8 10 20 100 1
    5 7 8 8 10 20 100 1
    1 5 7 8 8 10 20 100


    >>> sort_arg = "double_selection"


    >>> values_tmp = copy.copy(values)
    >>> _c = get_sort_instance(sort_arg)
    >>> _c.sort(values_tmp, num ,lambda x, y: x < y)
    selection_sort by double_list
    [10, 5, 7, 8, 8, 20, 100, 1]
    1 5 7 8 8 10 20 100
    3
    """


if __name__ == '__main__':

    import doctest
    doctest.testmod()
