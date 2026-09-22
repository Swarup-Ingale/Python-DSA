# class student:
#     def accept(self,roll,name,percent):  #self is use to accept 
#         self.roll = roll
#         self.name = name
#         self.percent = percent
#     def display(self):
#         print(self.roll)
#         print(self.name)
#         print(self.percent)

# s1=student()  #s1 is instance variable/pointer and student is object
# s1.accept(1,"abc",90)
# s1.display()
# print(id(s1.accept(1,"abc",90)))
# print(id(s1.display()))

#for constructor
# class student:
#     def __init__(self,roll,name,percent):  #self is use to accept 
#         self.roll = roll
#         self.name = name
#         self.percent = percent
#     def display(self):
#         print(self.roll)
#         print(self.name)
#         print(self.percent)

# s1=student(1, "Eacd",12.43)  #s1 is instance variable/pointer and student is object
# #s1.accept(1,"abc",90)
# s1.display()


#Static variable and static method
# class student:
#     clg ="acp"  #global static variable /static class variable
#     def __init__(self,roll,name):  #self is use to accept 
#         self.roll = roll  #instance/ object/ member variable
#         self.name = name
#         #self.clg = clg
#     def display(self):
#         print(self.roll)
#         print(self.name)
#         print(self.clg)
#         print(student.clg)

# s1=student(1, "Eacd")  #s1 is instance variable/pointer and student is object
# s1.display()

# s2=student(2,"xyz")
# s2.display()
# s3=student(3,"qwe")
# s3.display()
# print(student.clg)
# s1.clg="xyz"
# print(s1.clg)
# #print(student.roll)  #Error

# print(s2.clg);print(s3.clg)



# class student:
#     def accept(self,roll,name,percent):  #self is use to accept 
#         self.roll = roll
#         self.name = name
#         self.percent = percent
#     def display(self):
#         print(self.roll)
#         print(self.name)
#         print(self.percent)

# # Inheritance

#SIngle inheritance
# class Parent:
#     def home(self):
#         print("Parents home()")

# class child(Parent):
#     pass

# c =child();
# c.home()


#multi level inheritance
# class grandparent:
#     def car(self):
#         print("Car")
# class Parent(grandparent):
#     def home(self):
#         print("Parents home()")

# class child(Parent):
#     pass

# c= child();
# c.car();c.home()

#multiple inheritance

# class parent1:
#     def msg1(self):
#         print("From p1")

# class parent2:
#     def msg2(self):
#         print("From p2")


# class child(parent1,parent2):
#     pass       

# c=child()
# c.msg1()
# c.msg2()


# class parent1:
#     def msg1(self):
#         print("From p1")

# class parent2:
#     def msg1(self):
#         print("From p2")


# class child(parent2,parent1):
#     pass       

# c=child()
# c.msg1()


#Muti
##Incomplete code

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age =age

# class Student(Person):
#     def _init__(self,name,age,roll,m1,m2,m3):
#         super().self.name
#         self.roll = roll
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     def displayS(self):
#         print("Name":+name)
#         total = m1+m2+m3
#         print(total)
#         avg = total//3
#         print(avg)
# class Teacher(Person):
#     def __init__(self,sal,dep):
#         self.sal =sal
#         self.dep =dep
        
# s= Student("name",13,20,20,20)

# class Ex:
#     def add(s,a,b):
#         print("addition of 2 numbers",a+b)
#     def add(s,x,y,z):
#         print("addition of 3 numbers",x+y+z)

# e = Ex()
# e.add(1,2,4)
# e.add(1,2)    #error -function replacement


# class Ex:
#     def add(s,a,b,c==None):
#         if(c==None):
#             print("Addition of 2 numbers is ",a+b)
#         else:
#             print("Addition of 3 numbers is ",a+b+c)


# e = Ex()
# e.add(1,2)
# e.add(1,4,3)


# class A:
#     def add(s,a,b):
#         print(a+b)
# class B(A):
#     def add(s,a,b,c):
#         print(a+b+c)

# a =B()
# a.add(1,2,3)
# a.add(1,2) #error child class function replacement

#Method  Over-riding
# class Parent:
#     def car(self):
#         print("car")

# class child(Parent):
#     pass
# c = child()
# c.car()

# class Parent:
#     def car(self):
#         print("car")

# class child(Parent):
#     def car(self):
#         print("xyz")
# c = child()
# c.car()

# class Bxnk:
#     def __init__(self,balance):
#         self.balance = balance
#     def deposite(self,amt):
#         self.__balance = self.__balance + amt

#     def withdraw(self,balance):
#         if amt > self.__balance:
#             print("Insufficient")
#         else:
#             self.balance -= amt
#             print(amt,"is withdraw")
#     def getbalance(self):
#         print(self.__balance)

# b = Bxnk()
# b.deposite(120000)
# b.getbalance()        
        


from abc import ABC,abstractmethod

# class Ex(ABC):
#     @abstractmethod    #decorators
#     def task(s):
#         pass #Empty method / abstract method
#     def sal(s):
#         print("Sal credited")
# class child(Ex):
#     def task(s):
#         print("complete")

# a = child()
# a.sal()


#linked lsit

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next  = None
# start = Node(10)
# start.next = Node(20)
# start.next.next=Node(30)
# start.next.next.next=Node(40)
# print(start.data,end="->")
# print(start.next.data,end="->");print(start.next.next.data,end="->")
# print(start.next.next.next.data,end="->None")


class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None


class LinkedList:
    def __init__(self):
        self.start = None

    def create_node(self):
        data=int(input("Enter data=="))
        return Node(data)

    def insert_node_at_first(self):
        if self.start == None:
            self.start=self.create_node()
        else:
            temp = self.create_node()
            temp.next=self.start
            self.start=temp

    def insert_node_at_last(self):
        s = self.start
        if s == None:
            self.start = self.create_node()
        else:
            while(s.next !=None):
                s=s.next
            s.next = self.create_node()

    
    def print_list(self):
        s = self.start
        if s==None:
            print("Nothing")
        while(s!=None):
            print(s.data,end="--")
            s=s.next
        print(None)

l = LinkedList()
l.print_list()
l.insert_node_at_first()
l.insert_node_at_first()
l.insert_node_at_last()
l.insert_node_at_first()
l.insert_node_at_first()
l.insert_node_at_first()
l.insert_node_at_last()
l.print_list()