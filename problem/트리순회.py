V, E = map(int, input().split())
tree = [[0] * 3 for _ in range(V+1)]
temp = list(map(int, input().split()))

for i in range(E):
    n1 = temp[i*2]
    n2 = temp[i*2+1]
    if not tree[n1][0]:
        tree[n1][0] = n2
    else:
        tree[n1][1] = n2
    tree[n2][2] = n1

def preorder(node):
    if node != 0:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        cnt += 1
        inorder(tree[node][1])


def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        cnt += 1