import double_list
import copy


def list_insert_sort(values_list, length_list, comp_func):
    """
    >>> list = [5, 2, 4, 6, 1, 3]

    >>> list_tmp = copy.copy(list)
    >>> list_insert_sort(list_tmp, 6, lambda x, y: x > y)
    insert_sort
    [2, 5, 4, 6, 1, 3]
    [2, 4, 5, 6, 1, 3]
    [2, 4, 5, 6, 1, 3]
    [1, 2, 4, 5, 6, 3]
    [1, 2, 3, 4, 5, 6]

    >>> list_tmp = copy.copy(list)
    >>> list_insert_sort(list_tmp, 6, lambda x, y: x < y)
    insert_sort
    [5, 2, 4, 6, 1, 3]
    [5, 4, 2, 6, 1, 3]
    [6, 5, 4, 2, 1, 3]
    [6, 5, 4, 2, 1, 3]
    [6, 5, 4, 3, 2, 1]
    """

    print("insert_sort")
    for i in range(1, length_list):
        tmp = values_list[i]
        j = i-1
        while j >= 0 and comp_func(values_list[j], tmp):
            values_list[j+1] = values_list[j]
            j = j-1
        values_list[j+1] = tmp
        print(values_list)

    return


def list_bubble_sort(values_list, length_list, comp_func):
    """
    >>> list = [5, 2, 4, 6, 1, 3]

    >>> list_tmp = copy.copy(list)
    >>> list_bubble_sort(list_tmp, 6, lambda x, y: x < y)
    bubble_sort
    [5, 2, 4, 1, 6, 3]
    [5, 2, 1, 4, 6, 3]
    [5, 1, 2, 4, 6, 3]
    [1, 5, 2, 4, 6, 3]
    [1, 5, 2, 4, 3, 6]
    [1, 5, 2, 3, 4, 6]
    [1, 2, 5, 3, 4, 6]
    [1, 2, 3, 5, 4, 6]
    [1, 2, 3, 4, 5, 6]
    9

    >>> list_tmp = copy.copy(list)
    >>> list_bubble_sort(list_tmp, 6, lambda x, y: x > y)
    bubble_sort
    [5, 2, 4, 6, 3, 1]
    [5, 2, 6, 4, 3, 1]
    [5, 6, 2, 4, 3, 1]
    [6, 5, 2, 4, 3, 1]
    [6, 5, 4, 2, 3, 1]
    [6, 5, 4, 3, 2, 1]
    6
    """

    print("bubble_sort")
    flag = 1
    exchange_count = 0
    while flag == 1:
        flag = 0
        for j in range(length_list-1, 0, -1):
            if comp_func(values_list[j], values_list[j-1]):
                tmp = values_list[j]
                values_list[j] = values_list[j-1]
                values_list[j-1] = tmp
                flag = 1
                exchange_count += 1
                print(values_list)

    print(exchange_count)
    return


def list_selection_sort(values_list, length_list, comp_func):
    """
    >>> list = [5, 2, 4, 6, 1, 3]

    >>> list_tmp = copy.copy(list)
    >>> list_selection_sort(list_tmp, 6, lambda x, y: x < y)
    selection_sort
    3

    >>> list_tmp = copy.copy(list)
    >>> list_selection_sort(list_tmp, 6, lambda x, y: x > y)
    selection_sort
    4

    """
    print("selection_sort")

    exchange_count = 0
    exchange_flag = 0
    for i in range(length_list):
        minj = i
        for j in range(i, length_list, 1):
            if comp_func(values_list[j], values_list[minj]):
                minj = j
                exchange_flag = 1
        tmp = values_list[i]
        values_list[i] = values_list[minj]
        values_list[minj] = tmp
        if exchange_flag:
            exchange_count += 1
        exchange_flag = 0
    print(exchange_count)
    return


def change_list_to_double(before_list, double_list):
    length_list = len(before_list)
    for i in range(length_list-1, -1, -1):
        double_list.insert(before_list[i])
    return


def double_list_insert_sort(values_list, length_list, comp_func):
    """
    >>> list = [5, 2, 4, 6, 1, 3]
    >>> list_tmp = copy.copy(list)
    >>> double_list_insert_sort(list_tmp, 6,lambda x, y: x > y)
    insert_sort by double_list
    5 2 4 6 1 3
    2 5 4 6 1 3
    2 4 5 6 1 3
    2 4 5 6 1 3
    1 2 4 5 6 3
    1 2 3 4 5 6


    >>> list_tmp = copy.copy(list)
    >>> double_list_insert_sort(list_tmp, 6,lambda x, y: x < y)
    insert_sort by double_list
    5 2 4 6 1 3
    5 2 4 6 1 3
    5 4 2 6 1 3
    6 5 4 2 1 3
    6 5 4 2 1 3
    6 5 4 3 2 1
    """
    print("insert_sort by double_list")

    sort_list = double_list.Double_List()

    change_list_to_double(values_list, sort_list)

    sort_list.all_node_show()

    tmp_node = sort_list.head_node

    for i in range(1, length_list, 1):
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


def double_list_bubble_sort(values_list, length_list, comp_func):
    """
    >>> list = [5, 2, 4, 6, 1, 3]

    >>> list_tmp = copy.copy(list)
    >>> double_list_bubble_sort(list_tmp, 6,lambda x, y: x < y)
    bubble_sort by double_list
    1 2 3 4 5 6
    9

    >>> list_tmp = copy.copy(list)
    >>> double_list_bubble_sort(list_tmp, 6,lambda x, y: x > y)
    bubble_sort by double_list
    6 5 4 3 2 1
    6

    >>> list = [5, 3, 2, 4, 1]

    >>> list_tmp = copy.copy(list)
    >>> double_list_bubble_sort(list_tmp, 5,lambda x, y: x < y)
    bubble_sort by double_list
    1 2 3 4 5
    8
    """

    print("bubble_sort by double_list")

    sort_list = double_list.Double_List()

    change_list_to_double(values_list, sort_list)

    tmp_node = sort_list.head_node.prev

    flag = 1
    exchange_count = 0

    tmp_node = tmp_node.prev

    while flag:
        flag = 0
        for j in range(length_list):
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


def double_list_selection_sort(values_list, length_list, comp_func):
    # insert???????????????????????????????????????????????????
    # ?????????????????????????????????????????????????????????????????????
    """
    >>> list = [5, 2, 4, 6, 1, 3]
    >>> list_tmp = copy.copy(list)
    >>> double_list_selection_sort(list_tmp, 6,lambda x, y: x > y)
    selection_sort by double_list
    1 2 3 4 5 6
    3

    >>> list_tmp = copy.copy(list)
    >>> double_list_selection_sort(list_tmp, 6,lambda x, y: x < y)
    selection_sort by double_list
    6 5 4 3 2 1
    4

    >>> list_tmp = copy.copy(list)
    >>> double_list_selection_sort(list_tmp, 6,lambda x, y: x > y)
    selection_sort by double_list
    1 2 3 4 5 6
    3

    """
    print("selection_sort by double_list")

    sort_list = double_list.Double_List()

    change_list_to_double(values_list, sort_list)

    tmp_node = sort_list.head_node
    j_tmp_node = tmp_node

    exchange_count = 0
    exchange_flag = 0

    for i in range(0, length_list):
        biggest_value = tmp_node.value

        for j in range(i, length_list):
            if comp_func(j_tmp_node.value, biggest_value):
                biggest_value = j_tmp_node.value
                exchange_flag = 1
            j_tmp_node = j_tmp_node.next

        sort_list.delete(biggest_value)
        sort_list.insert(biggest_value)
        if exchange_flag:
            exchange_count += 1
        else:
            tmp_node = tmp_node.next
        j_tmp_node = tmp_node
        exchange_flag = 0
    sort_list.all_node_show()
    print(exchange_count)

    return


# ?????????????????????

def is_stable(before_data, after_data):
    length = len(before_data)

    for i in range(length):
        for j in range(i+1, length):
            for a in range(length):
                for b in range(a+1, length):
                    # ????????? i???b j???a????????????????????????????????????
                    if before_data[i][1] == before_data[j][1] and \
                       before_data[i] == after_data[b] and \
                       before_data[j] == after_data[a]:
                        return False

    return True


def tramp_bubble(data_list, length_list):
    for i in range(length_list):
        for j in range(length_list-1, i, -1):
            if data_list[j][1] < data_list[j-1][1]:
                data_list[j], data_list[j-1] = data_list[j-1], data_list[j]

    return


def tramp_selection(data_list, length_list):
    for i in range(length_list):
        minj = i
        for j in range(i, length_list):
            if data_list[j][1] < data_list[minj][1]:
                minj = j

        data_list[i], data_list[minj] = data_list[minj], data_list[i]

    return


def print_tramp_list(data_list):
    for i in range(len(data_list)):
        mozi = ""
        for j in data_list[i]:
            mozi += str(j)
        if i < len(data_list) - 1:
            print(mozi, end=" ")
        else:
            print(mozi)

    return


def separate_suit_num(to_separate_list):
    length_list = len(to_separate_list)
    for i in range(length_list):
        to_separate_list[i] = [(to_separate_list[i])[:1],
                               (to_separate_list[i])[1:]]
    return


def tramp_sort(data_list, length_list):
    """
    >>> list = ["H4", "C9", "S4", "D2", "C3"]

    >>> tramp_sort(list, 5)
    D2 C3 H4 S4 C9
    Stable
    D2 C3 S4 H4 C9
    Not stable
    """

    separate_suit_num(data_list)
    list_after = copy.copy(data_list)
    tramp_bubble(list_after, length_list)
    print_tramp_list(list_after)
    if is_stable(data_list, list_after):
        print("Stable")
    else:
        print("Not stable")

    list_after = copy.copy(data_list)
    tramp_selection(list_after, length_list)
    print_tramp_list(list_after)
    if is_stable(data_list, list_after):
        print("Stable")
    else:
        print("Not stable")

    return


class tramp_node(double_list.Node):
    def __init__(self, value, suit):
        super(tramp_node, self).__init__(value)
        self.suit = suit


class tramp_double(double_list.Double_List):
    def insert(self, value, suit):
        # ????????????????????????????????????????????????????????????
        new_node = tramp_node(value, suit)
        tmp_node = self.head_node

        # head_node????????????????????????????????????
        # head????????? = ??????0?????????
        if not tmp_node:
            new_node.prev = new_node
            new_node.next = new_node
            self.head_node = new_node
            return

        new_node.next = self.head_node
        new_node.prev = self.head_node.prev
        self.head_node.prev.next = new_node
        self.head_node.prev = new_node
        self.head_node = new_node

        return

    def delete(self, value, suit):
        tmp_node = self.head_node
        # ??????????????????????????????
        if not tmp_node:
            print("List is empty.")
            return
        while tmp_node:
            # ????????????
            if tmp_node.value == value and \
                    tmp_node.suit == suit:
                tmp_node.prev.next = tmp_node.next
                tmp_node.next.prev = tmp_node.prev
                # ????????????????????????????????????????????????????????????
                if tmp_node == self.head_node:
                    self.head_node = self.head_node.next
                return

            tmp_node = tmp_node.next

            # ??????????????????
            if tmp_node == self.head_node:
                return
        return

    def all_node_show(self):
        tmp_node = self.head_node
        if self.head_node.next == self.head_node:
            print(tmp_node.suit, end="")
            print(tmp_node.value)
            return

        print(tmp_node.suit, end="")
        print(tmp_node.value, end=" ")
        tmp_node = tmp_node.next

        while tmp_node:
            if tmp_node.next == self.head_node:
                print(tmp_node.suit, end="")
                print(tmp_node.value)
                return

            else:
                print(tmp_node.suit, end="")
                print(tmp_node.value, end=" ")
                tmp_node = tmp_node.next
        return

    def change_list_to_double(self, before_list):
        length_list = len(before_list)
        for i in range(length_list-1, -1, -1):
            self.insert(before_list[i][1], before_list[i][0])
        return

    def change_double_to_list(self):
        tmp_node = self.head_node
        return_list = []
        mozi = str(tmp_node.suit) + str(tmp_node.value)
        return_list.append(mozi)
        tmp_node = tmp_node.next

        while not tmp_node == self.head_node:
            mozi = str(tmp_node.suit) + str(tmp_node.value)
            return_list.append(mozi)
            tmp_node = tmp_node.next

        return return_list

    def tramp_double_bubble(self, data_list, length_list):
        self.change_list_to_double(data_list)

        tmp_node = self.head_node.prev
        tmp_node = tmp_node.prev
        flag = 1

        while flag:
            flag = 0
            for j in range(length_list):
                if tmp_node.value < tmp_node.prev.value and \
                        tmp_node != self.head_node:

                    tmp_value = tmp_node.value
                    tmp_suit = tmp_node.suit

                    tmp_node.value = tmp_node.prev.value
                    tmp_node.suit = tmp_node.prev.suit

                    tmp_node.prev.value = tmp_value
                    tmp_node.prev.suit = tmp_suit

                    flag = 1
                tmp_node = tmp_node.prev
        self.all_node_show()

        return

    def tramp_double_selection(self, data_list, length_list):

        self.change_list_to_double(data_list)

        tmp_node = self.head_node
        j_tmp_node = tmp_node

        for i in range(0, length_list):
            biggest_value = tmp_node.value
            biggest_suit = tmp_node.suit

            for j in range(i, length_list):
                if j_tmp_node.value > biggest_value:
                    biggest_value = j_tmp_node.value
                    biggest_suit = j_tmp_node.suit
                    exchange_flag = 1

                j_tmp_node = j_tmp_node.next

            self.delete(biggest_value, biggest_suit)
            self.insert(biggest_value, biggest_suit)
            if exchange_flag:
                pass
            else:
                tmp_node = tmp_node.next
            j_tmp_node = tmp_node
            exchange_flag = 0
        self.all_node_show()

        return

    def separate_suit_num(self, to_separate_list):
        length_list = len(to_separate_list)
        for i in range(length_list):
            to_separate_list[i] = [(to_separate_list[i])[:1],
                                   (to_separate_list[i])[1:]]
        return


def double_list_tramp_sort(data_list, length_list):
    """
    >>> list = ["H4", "C9", "S4", "D2", "C3"]
    >>> double_list_tramp_sort(list, 5)
    D2 C3 H4 S4 C9
    Stable
    D2 C3 S4 H4 C9
    Not stable
    """

    sort_list = tramp_double()

    separate_suit_num(data_list)
    list_tmp = data_list
    sort_list.tramp_double_bubble(list_tmp, length_list)
    list_after = sort_list.change_double_to_list()
    separate_suit_num(list_after)
    if is_stable(data_list, list_after):
        print("Stable")
    else:
        print("Not stable")

    # ???????????????????????????
    sort_list = tramp_double()

    list_tmp = data_list
    sort_list.tramp_double_selection(list_tmp, length_list)
    list_after = sort_list.change_double_to_list()
    separate_suit_num(list_after)
    if is_stable(data_list, list_after):
        print("Stable")
    else:
        print("Not stable")

    return


if __name__ == '__main__':
    import doctest
    doctest.testmod()
