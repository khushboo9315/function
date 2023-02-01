# '''     1. Write a Python function to find the Max of three numbers.     '''


# # def maximum(a,b,c):
# #     max=0
# #     if a>b:
# #         max=a
# #     else:
# #         max=b
# #         if max>c:
# #             max=max
# #         else:
# #             max=c
# #     print(max)
# # maximum(int(input()),int(input()),int(input()))


# '''     2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20     '''

# # def func(a):
# #     sum=0
# #     for i in (a):
# #         sum+=i
# #     print(sum)
# # func([3,4,5,6,7])
    

# '''3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336          '''

# # def sum(a):
# #     mul=1
# #     for i in a:
# #         mul=mul*i
# #     return mul
# # print(sum([8, 2, 3, -1, 7]))

# '''     4. Write a Python function to reverse a string
# Sample String : "1234abcd"
# Expected Output : "dcba4321"     '''

# def rev(a):
#      revs=''


#      for i in range(len(a)-1,-1,-1):
#           revs+=a[i]

        
#      return  revs
# c=rev("khushi")
# print(c)


'''     5. Write a Python function to calculate the factorial of a number (a non-negative integer). The
function accepts the number as an argument.     '''

# def num(a):
#     fac=1
#     for i in range (1,a+1):
#         fac*=i
#     return fac
# print(num(5))

'''     6. Write a Python function to check whether a number falls in a given range. Function
argements are (u, l, n) where u=upper limit, l = lowr limit and n = number to search for.     '''

# def check(l,u,n):
#     for i in range(l,u+1):
#         if i==n:
#             return n
#     else:
#         return 0
# a= check(50,100,56)
# print(check(int(input()),int(input()),int(input())))


'''     7. Write a Python function that accepts a string and calculate the number of upper case letters
and lower case letters.Sample String : 'The quick Brow Fox Jumps Over the Lazy Dog.
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12     '''

# def check(a):
#     l=0
#     u=0
#     for i in a:
#         if i>="a" and i<="z":
#             l+=1
#         elif i>="A" and i<="Z":
#             u+=1
#     print(l)
#     print(u)
# check(input())


'''     8. Write a Python function that takes a list and returns a new list with unique elements of the first
list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]     '''

# def list(a):
#     b=[]
#     for i in (a):
#         if i not in (b):
#                 b.append(i)
#     print(b)
# list([1,2,3,3,3,3,4,5])

'''     9. Write a Python function that takes a number as a parameter and check the number is prime
or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no
# positive divisors other than 1 and itself.     '''


# def prime(a):
#      c=0
#      for i in range(1,a//2+1):
#          if a%i==0:
#           c+=1
#      if c==1:

#           return 'YES'
#      else:
#           return 'NO'
# print(prime(int(input())))

'''     10. Write a Python function to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]     '''

# def even(a):
#     b=[]
#     for i in (a):
#         if i%2==0:
#             b.append(i)
#     return b
# print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))

'''      11. Write a Python function to check whether a number is perfect or not.
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to
the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the
number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is
half the sum of all of its positive divisors (including itself).
     '''

# def perfect(a):
#     sum=0
#     for i in range(1,(a//2)+1):
#         if a%i==0:
#             sum+=i
#     if sum ==a:
#         return True
#     return 
# print(perfect(int(input())))
# 


'''     12. Write a Python function that checks whether a passed string is palindrome or not.       '''

# def rev(a):
#     b=""
#     for i in range(len(a)-1,0-1,-1):
#         b+=a[i]
#     if b==a:
#         return YES
#     return NO 
# print(rev(input()))



'''     14. Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"     '''

# def check(a):
#     b="abcdefghijklmnopqrstuvwxyz"
#     for i in b:
#         if i not in a:
#             return False
#     return True
# str="The quick brown fox jumps over the lazy dog"
# print(check(str))

'''     15. Write a Python program that accepts a hyphen-separated sequence of words as input and
prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow     '''

# a="green-red-yellow-black-white"
# b=a.split("-")
# print(b)
# b.sort()
# print(b)
# for i in range (len(b)):
#      if i==len(b)-1:
#           print(i)
#      else:
#           print(b[i],end="-")

            
'''16. Write a Python function to create and print a list where the values are square of numbers
between 1 and 30 (both included).'''

# def square(a):
#      for i in range(1,a+1):
#           c=i*i
#           print(c,end=",")
# square(30)

'''     13. Write a Python function that prints out the first n rows of Pascal's triangle.
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
Sample Pascal's triangle :     '''

# 

def fac(a):
     mul=1
     for i in range(2,a+1):
          mul*=i
     return mul
# a=int(input("num:"))
# print(fac(a))
def pascal(a):
     s=a
     for i in range(a+1):
          for j in range(i+1):
               b=fac(i)//((fac(j))*(fac(i-j)))
               print(" "*s,b,end=" ")
          s-=1
          print()
pascal(int(input("num:")))

