class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_d(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def linked_append(self, data):
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size += 1

    def new_num(self, jump, cycle):
        current = self.head
        current = current.next
        for _ in range(cycle):
            for _ in range(jump-1):
                current = current.next
            tmp = current.get_d() + current.prev.get_d()
            new_node = Node(tmp)
            if current is self.head:
                self.tail = new_node
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1
            # self.print_data(self.size)
        self.print_data(self.size)


    def print_data(self, ran):
        if self.head is None:
            return
        # 정순
        # current = self.head
        # for _ in range(ran):
        #     print(current.get_d(), end=' ')
        #     current = current.next
        # print()
        #역순
        current = self.tail
        if self.size >= 10:
            ran = 10
        print('#{}'.format(tc),end=' ')
        for _ in range(ran):
            print(current.get_d(), end=' ')
            current = current.prev
        print()


for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    num = list(map(int, input().split()))
    my_linked = LinkedList()
    for i in num:
        my_linked.linked_append(i)
    my_linked.new_num(M,K)