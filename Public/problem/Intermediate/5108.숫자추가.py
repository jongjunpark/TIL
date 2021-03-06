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
        self.tail = None
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

    def add_data(self, idx, data):
        new_node = Node(data)
        current = self.head
        if current is None: # 비어있을 때
            self.head = new_node
            self.size += 1
            return
        if idx == 0:
            new_node.next = current
            self.head = new_node
        elif idx >= self.size:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            pre = None
            for _ in range(idx):
                pre = current
                current = current.next
            pre.next = new_node
            new_node.next = current
        self.size += 1

    def print_data(self, idx):
        current = self.head
        if current is None:
            return
        for _ in range(idx):
            current = current.next
        print('#{} {}'.format(tc,current.get_d()))

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    num = list(map(int, input().split()))
    plus = [list(map(int, input().split())) for _ in range(M)]
    my_linked = LinkedList()
    for i in num:
        my_linked.linked_append(i)
    for j in range(M):
        my_linked.add_data(plus[j][0],plus[j][1])
    my_linked.print_data(L)