class Node:     # 데이터를 저장하는 변수역할
    def __init__(self, data):
        self.data = data
        self.next = None    # 다음 노드의 주소는 없을 수도 있어서 None을 기본적으로 설정 (리스트의 끝인 경우)

    def get_d(self):
        return self.data

    def change_d(self,data):
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def linked_append(self, data):
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = new_node
            self.size += 1
            return
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1

    def insert(self, idx, data):
        new_node = Node(data)
        current = self.head
        if idx == 0:
            new_node.next = current
            self.head = new_node
        else:
            pre = None
            for _ in range(idx):
                pre = current
                current = current.next
            pre.next = new_node
            new_node.next = current
        self.size += 1

    def check(self, data, arr):
        current = self.head
        idx = 0
        while current.get_d() <= data:
            idx += 1
            if current.next is None:
                break
            current = current.next

        for i in range(1,N+1):
            self.insert(idx, arr[-i])
        # self.print_data()

    def print_data(self):
        current = self.head
        while current is not None:
            print(current.get_d(), end=' ')
            current = current.next
        print()

    def print_data_reverse_ten(self):
        global result
        current = self.head
        start = self.size - 10
        for k in range(start):
            current = current.next
        for i in range(10):
            result.append(current.get_d())
            current = current.next

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num = [list(map(int, input().split())) for _ in range(M)]
    my_linked = LinkedList()
    for i in num[0]:
        my_linked.linked_append(i)
    for j in range(1,M):
        my_linked.check(num[j][0], num[j])
    result = []
    my_linked.print_data_reverse_ten()
    print('#{}'.format(tc), end=' ')
    for k in range(1,11):
        print(result[-k], end=' ')
    print()