import sys

n = int(input())
tree = {}
for _ in range(n):
    node,left,right = input().split()
    tree[node] = [left,right]
# 전위
def preorder(i):
    if i != '.' :
        print(i,end='')
        preorder(tree[i][0])
        preorder(tree[i][1])
#중위
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])
# 후위
def post(root):
    if root != '.':
        post(tree[root][0])
        post(tree[root][1])
        print(root,end='')
preorder('A')
print()
inorder('A')
print()
post('A')
