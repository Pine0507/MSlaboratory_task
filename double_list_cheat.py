# deque使ったからすぐできたやつ

from collections import deque

'''doctest
   >>> 7
   >>> insert 5
   >>> insert 2
   >>> insert 3
   >>> insert 1
   >>> delete 3
   >>> insert 6
   >>> delete 5
'''

if __name__ == '__main__':
    command_number = int(input())
    list = deque()

    for i in range(command_number):
        cmdline = input().split()

        if cmdline[0] == "insert":
            list.appendleft(cmdline[1])
        elif cmdline[0] == "delete":
            list.remove(cmdline[1])
        elif cmdline[0] == "deleteFirst":
            list.popleft()
        elif cmdline[0] == "deleteLast":
            list.pop()

    print(" ".join(list))
