#STACK IS LIFO {array}
stack=[]
def push():
    element=int(input("enter the element"))
    stack.append(element)
    print(stack)
def check_empty(stack):
    return len(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("remove element",e)
        print(stack)
def peek():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print('top is',e)
def display():
    print(stack)   
while True:
    print("select operation 1.push 2.pop 3.display 4.peek")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        break
    else:
        print("enter a valid element")
        
