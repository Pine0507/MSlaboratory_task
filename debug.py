import double_list


def double_list_bubble_sort(values_list, num):
    """
    >>> list = [5,2,4,6,1,3]
    >>> double_list_bubble_sort(list,6)
    bubble_sort by double_list
    1 2 3 4 5 6
    9
    """

    print("bubble_sort by double_list")

    sort_list = double_list.Double_List()

    for i in range(num-1, -1, -1):
        sort_list.insert(values_list[i])

    tmp_node = sort_list.head_node.prev

    tmp_j_node = tmp_node

    flag = 1
    exchenge_count = 0

    tmp_j_node = tmp_j_node.prev
    tmp_node = tmp_node.prev

    print(tmp_node.value)
    sort_list.all_node_show()

    while flag:
        flag = 0
        for j in range(num):
            if tmp_j_node.value < tmp_j_node.prev.value:

                tmp_value = tmp_j_node.value
                tmp_j_node.value = tmp_j_node.prev.value
                tmp_j_node.prev.value = tmp_value
                flag = 1
                exchenge_count += 1
            tmp_j_node = tmp_j_node.prev
            tmp_node = tmp_node.prev
            print("a")
    sort_list.all_node_show()
    print(exchenge_count)

    return
