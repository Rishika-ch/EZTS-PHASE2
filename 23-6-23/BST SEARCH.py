#Write a program to perform search operation on certain node in bst.
#100,70,50,60,9,-3
#BST-INSERT
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root

def search(root,key):
    #Base cases root is null key is present
    if root is None or root.val==key:
        return root
    #key is greater than root's key
    if root.val<key:
        return search(root.right,key)
    #key is smaller than root's key
    return search(root.left,key)

x=Node(50)
x=insert(x,30)
x=insert(x,20)
x=insert(x,40)
x=insert(x,70)
x=insert(x,60)
x=insert(x,80)
search(x,20)
