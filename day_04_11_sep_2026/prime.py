# #print a prime number from 1 to 10000000
# i=2
# # n=10

# # while(i<10):
# #     j=2
# #     while(j<i):
# #         if(i%j == 0):
# #             break
# #         j=j+1
# #     i=i+1
# #     print(i)

# #
# i=7
# for i in range(2,10):
#     for j in range(2,i):
#         if(i%j==0):
#             break
# else:
#     print(i)



#enter name from user and print it in pyramid

# user = input("Enter name::")
# # m=1
# s= len(user)
# for j in range(s):  
#     for k in range(s):
#         print(" ", end="")
#     for i in range(j+1):
#         print(user[i] , end=" ")
#     print()
#     # m += 1
#     s -= 1

# m = 1
# s = 4
# for i in range(5):
#     for j in range(s):
#         print(" ", end="")
#     for k in range(m):
#         print(k+1 , end=" ")
#     print()
#     m += 1
#     s -= 1

# m = 1
# for i in range(5):
#     for j in range(m):
#         print("#", end="")
#     print()
#     m += 1
    

# for i in range(s):
#     for j in range(s):
#         print(" ", end="")
#     for k in range(m):
#         print("* ", end="")
#     print()
#     m += 1
#     s -= 1


#OOPS

# class A:
#     def add(self,a,b):  #s and self are same 
#         print(a+b)
#     def sub(self,a,b):       #sel(supported variable) is mandatory
#         print(a-b)

# class B(A):
#     def mul(s,a,b):
#         print(a*b)

# class C(B):
#     def mod(s,a,b):
#         print(a%b)

# class D(B):
#     def p21(s,a):
#         print(a)
# obj1 = C()
# obj1.add(1,2)
# obj1.sub(2,1)
# obj1.mul(2,3)
# obj1.mod(4,2)
# obj1.d21("xyz")

import math

class Calculator:
    def add(s,a,b):
        print(a+b)
    def sub(s,a,b):
        print(a-b)
    def mul(s,a,b):
        print(a*b)
    def power(s,a,b):
        print(a**b)
    def div(s,a,b):
        print(a/b)


        
class SciCal(Calculator):
    def factorial(s,a):
        print(math.factorial(a))
    def fibonacci(s,a):
        n1 =0
        n2 =1
        for i in range(a):
            print(n1, end=" ")
            n1,n2=n2,n1+n2
    def is_prime(s,a):
        if a <= 1:
            return False
        for i in range(2, int(math.sqrt(a)) + 1, 6):
            if a % i == 0 or a % (i + 2) == 0:
                return False
        return True 

obj =Calculator()
obj1= SciCal()
obj1.add(2,3)
obj1.sub(4,3)
obj1.div(4,2)
obj1.factorial(5)
obj.mul(3,6)
obj1.fibonacci(6)
