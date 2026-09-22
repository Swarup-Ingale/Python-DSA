# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next  = None


# class LinkedList:
#     def __init__(self):
#         self.start = None

#     def create_node(self):
#         data=int(input("Enter data : "))
#         return Node(data)

#     def insert_node_at_first(self):
#         if self.start == None:
#             self.start=self.create_node()
#         else:
#             temp = self.create_node()
#             temp.next=self.start
#             self.start=temp

#     def insert_node_at_last(self):
#         s = self.start
#         if s == None:
#             self.start = self.create_node()
#         else:
#             while(s.next != None):
#                 s=s.next
#             s.next = self.create_node()
#     def delete_at_start(self):
#         if self.start == None:
#             print("Nothing to Delete")
#         else:
#             s = self.start
#             self.start = self.start.next
#             s.next = None
#             s = None

#     def delete_from_last(self):
#         if self.start == None:
#             print("Nothing to Delete")
#         elif self.start.next == None:
#             self.start = None
#         else:
#             s = self.start
#             while s.next.next != None:
#                 s = s.next
#             s.next = None
    
#     def print_list(self):
#         s = self.start
#         if s==None:
#             print("Nothing")
#         while(s!=None):
#             print(s.data,end="--")
#             s=s.next
#         print(None)

#     def insert_in_between(self):
#         index = int(input("Enter the index: "))
#         if index < 1:
#             print("Invalid Index")
#         elif index == 1:
#             return self.insert_node_at_first()
#         elif index > 1:
#             s = self.start
#             for i in range(1, index - 1):
#                 if s is None or s.next is None:
#                     print("Index out of bound")
#                     return
#                 s = s.next

#             temp = self.create_node()
#             temp.next = s.next
#             s.next = temp

#     def delete_in_between(self):
#         index = int(input("Enter the deletion node: "))
#         if index < 1:
#             print("Invalid index")
#         elif index == 1:
#             return self.delete_at_start()
#         elif index > 1:
#             s = self.start
#             for i in range(1, index - 1):
#                 if s is None or s.next is None:
#                     print("Index out of bound")
#                     return
#                 s = s.next
#             if s.next is not None:
#                 s1 = s.next
#                 s.next = s.next.next
#                 s1.next, s1 = None, None

#     def find_node(self):
#         target = int(input("ENter the Target: "))
#         s = self.start
#         if s == None:
#             print("Nothing to find MF")
#         elif s.next.data == target:
#             print("Found")
#         else:
#             while s != None:
#                 if s.data == target:
#                     print("Data Found !!!!!!!!!")
#                     return
#                 s = s.next
#             print("Data not found :(")

# l = LinkedList()
# l.print_list()
# l.insert_node_at_first()
# l.insert_node_at_first()
# l.insert_node_at_last()
# l.insert_node_at_first()
# l.insert_node_at_first()
# l.insert_node_at_first()
# l.insert_node_at_last()
# l.print_list()
# l.delete_at_start()
# l.insert_in_between()
# l.delete_in_between()
# l.print_list()
# l.find_node()
# l.print_list()

# DOUBLY LINKED LIST

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next  = None

# class DLL:
#     def __init__ (self):
#         self.start = None

#     def create_node(self):
#         data = int(input("Enter Data: "))
#         return Node(data)

#     def insert_at_first(self):
#         if self.start == None:
#             self.start = self.create_node()

#         else:
#             temp = self.create_node()
#             temp.next = self.start
#             self.start = temp
#             self.start.next.prev = self.start

#     def display_node(self):
#         if self.start == None:
#             print("nothing to print")

#         else:
#             s = self.start
#             while s != None:
#                 print(s.data, end="<-->")
#                 s = s.next
#             print(None)

#     def insert_at_last(self):
#         if self.start == None:
#             self.start = self.create_node()

#         else:
#             s = self.start
#             while s.next != None:
#                 s = s.next
#             s.next = self.create_node()
#             s.next.prev = s

#     def reverse(self):
#         if self.start == None:
#             print("No node available")

#         else:
#             s = self.start
#             while s.next != None:
#                 s = s.next

#             while s != None:
#                 print(s.data, end="<-->")
#                 s = s.prev

#     def delete_from_first(self):
#         if self.start == None:
#             print("Nothing to Delete")
#         else:
#             s = self.start
#             self.start = self.start.next
#             s.next = None
#             s = None
#             s.prev = None

#     def delete_from_last(self):
#         if self.start == None:
#             print("Nothing to delete")
#         else:
#             s = self.start
#             while s.next != None:
#                 s = s.next
#             s.next = None
#             s.prev.next = None

# d = DLL()
# d.insert_at_first()
# d.insert_at_first()
# d.insert_at_first()
# # d.insert_at_last()
# d.display_node()
# d.delete_from_last()

# Circular Linked List:

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next  = None

# class CLL:
#     def __init__ (self):
#         self.start = None

#     def create_node(self):
#         data = int(input("ENter the Data: "))
#         return Node(data)

#     def insert_at_fisrt(self):
#         if self.start == None:
#             self.start = self.create_node()
#             self.start.next = self.start
#         else:
#             s = self.create_node()
#             s.next = self.start
#             self.start = s

#     def display_cll(self):
#         if self.start == None:
#             print("Nothing to Print")
#         else:
#             s = self.start
#             while True:
#                 print(s.data)
#                 s = s.next
#                 if s.next == self.start:
#                     break

#     def insert_at_last(self):
#         if self.start == None:
#             self.start = self.create_node()
#         else:
#             s = self.start
#             while s.next != None:
#                 # Complete at Home

# STACK

# Stack Using Array / List (Fixed Size)

# class Stack:
#     def __init__ (self, size):
#         self.stack=[None] * size
#         self.size = size
#         self.top = -1

#     def push(self, data):
#         if self.is_full():
#             print("Stack is Full")
#         else:
#             self.top += 1
#             self.stack[self.top] = data
#             print(data, "Entered")

#     def pop(self):
#         if self.is_empty():
#             print("Nothing to delete")
#         else:
#             a = self.stack[self.top]
#             self.stack[self.top] = None
#             self.top -= 1
#             print(a, "is deleted")

#     def is_empty(self):
#         return self.top == -1

#     def is_full(self):
#         return self.top == self.size - 1

#     def peek(self):
#         print(f" THe top element is : self.stack[self.top]")

#     def display(self):
#         print(self.stack)

# s = Stack(5)
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.display()
# s.push(10)
# s.pop()
# s.pop()
# s.display()
# s.push(10)
# s.display()

# Stack using Linked List:

# Solve at home

# QUEUE

# Circular Linked List

# class Queue:
#     def __init__ (self, size):
#         self.size = size
#         self.queue = [None] * size
#         self.front = -1
#         self.rear = -1

#     def enqueue(self, data):
#         if self.is_full():
#             print("Queue Overflow")

#         elif self.is_empty():
#             self.front = 0
#             self.rear = 0
#             self.queue[self.rear] = data
#             print(data, "is inserterd")

#         else:
#             self.rear += 1
#             self.queue[self.rear] = data
#             print(data, "is inserterd")

#     def dequeue(self):
#         if self.is_empty():
#             print("Nothing to delete")

#         else:
#             a = self.queue[self.front]
#             self.queue[self.front] = None
#             print(a, "is deleted")

#     def is_full(self):
#         return self.rear == self.size - 1

#     def is_empty(self):
#         return self.front == -1

#     def display(self):
#         if self.is_empty():
#             print("Nothing to delete")
#         else:
#             print(self.queue)


# q = Queue(5)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.display()
# q.dequeue()
# q.dequeue()
# q.display()


# Circular Queue

class CQ:
    def __init__ (self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow")

        elif self.front == -1:
            self.front == 0
            self.rear == 0
            self.queue[self.rear] = data
            print(data, "inserted")

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print(data, "inserted")

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")

        else:
            a = self.queue[self.front]
            self.queue[self.front] = None
            print(a, "is deleted")

            if self.front == self.rear:
                self.front = -1
                self.rear = -1

            else:
                self.front = (self.front + 1) % self.size

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def display(self):
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size

q = CQ(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
q.dequeue()
q.dequeue()
q.display()