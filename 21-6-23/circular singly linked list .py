#single linked list implementation
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None

    """def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.next=None

    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range (pos-1):#1 iteration 1 happen
            temp=temp.next

        np.next=temp.next
        temp.next=np"""
        
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #temp = first node
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -> ")
                else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                temp=temp.next#establish link
obj=singlelinkedlist()
#node creation - initialising
n=Node(10)#so n,data in node class will be 10
obj.head=n      #displaying first node as head
n1=Node(20)
obj.head.next=n1#next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
print("Before insertion")
obj.display()
"""print()
print("After insertion at beginning")
obj.insert_beginning(5)
obj.display()
print()
print("After insertion at end")
obj.insert_end(70)
obj.display()
print()
print("After insertion at beginning")
obj.insert_position(3,1000)
obj.display()"""
