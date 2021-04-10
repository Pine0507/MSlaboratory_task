

# dequeの内容を自作したやつ

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Double_List:

    '''
    >>> list = Double_List()
    >>> list.insert(5)
    >>> list.insert(2)
    >>> list.insert(3)
    >>> list.insert(1)
    >>> list.delete(3)
    >>> list.insert(6)
    >>> list.delete(5)
    >>> list.all_node_show()
    6 1 2

    >>> list2 = Double_List()
    >>> list2.insert(5)
    >>> list2.insert(2)
    >>> list2.insert(3)
    >>> list2.insert(1)
    >>> list2.delete(3)
    >>> list2.insert(6)
    >>> list2.delete(5)
    >>> list2.deleteFirst()
    >>> list2.deleteLast()
    >>> list2.all_node_show()
    1

    '''

    def __init__(self):
        self.head_node = None

    def insert(self, value):
        # こいつをノード集合の先頭に持っていきたい
        new_node = Node(value)
        tmp_node = self.head_node

        # head_nodeはいつも一番最初のノード
        # headがない = 要素0のとき
        if not tmp_node:
            new_node.prev = new_node
            new_node.next = new_node
            self.head_node = new_node
            return

        """
        while not tmp_node == self.head_node:
            tmp_node = tmp_node.tail
        """

        new_node.next = self.head_node
        new_node.prev = self.head_node.prev
        self.head_node.prev.next = new_node
        self.head_node.prev = new_node
        self.head_node = new_node

        return

    def delete(self, value):
        tmp_node = self.head_node
        # 制約上必要ないが一応
        if not tmp_node:
            print("List is empty.")
            return
        while tmp_node:
            # 消すとき
            if tmp_node.value == value:
                tmp_node.prev.next = tmp_node.next
                tmp_node.next.prev = tmp_node.prev
                # 先頭を消した場合は先頭の次のやつを先頭に
                if tmp_node == self.head_node:
                    self.head_node = self.head_node.next
                return

            tmp_node = tmp_node.next

            # 要素がない時
            if tmp_node == self.head_node:
                return
        return

    def deleteFirst(self):
        # 制約上必要ないが一応
        if not self.head_node:
            print("List is empty")
        # 先頭だけの場合
        if self.head_node.next == self.head_node:
            self.head_node = None
            return

        self.head_node.prev.next = self.head_node.next
        self.head_node.next.prev = self.head_node.prev
        self.head_node = self.head_node.next
        return

    def deleteLast(self):
        # 制約上必要ないが一応
        if self.head_node is None:
            print("List is empty")
        # 先頭(末尾)だけの場合
        if self.head_node.next == self.head_node:
            self.head_node = None
            return
        self.head_node.prev.prev.next = self.head_node
        self.head_node.prev = self.head_node.prev.prev
        return

    def all_node_show(self):
        tmp_node = self.head_node
        if self.head_node.next == self.head_node:
            print(tmp_node.value)
            return

        print(tmp_node.value, end=" ")
        tmp_node = tmp_node.next

        while tmp_node:
            if tmp_node.next == self.head_node:
                print(tmp_node.value)
                return

            else:
                print(tmp_node.value, end=" ")
                tmp_node = tmp_node.next
        return


if __name__ == '__main__':
    import doctest
    doctest.testmod()
