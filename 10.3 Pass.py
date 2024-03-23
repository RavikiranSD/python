# for i in range(5):
#      #empty
# print("for sueful work")

# # O/P: print("for sueful work")
# #      ^
# # IndentationError: expected an indented block

# #now by using the pass:
# for i in range(5):
#     pass
# print("for some useful works")
#       #O/P:for some useful works

# #we can use for loop for if else statement also:
# for i in range(5):
# if 1>5:
# print("future using") 
#  #O/P:print("future using")
#  #     ^
#  #IndentationError: expected an indented b

# #using pass :
# for i in range(5):
#  if i>5:
#     pass
# print("future use")
# #O/P:future use


#Q1)WAP to find the sum of first n natural numbers(using for)
# n=5
# sum=0
# for i in range(1,n+1):        #here n+1 is written because in range (stop section) always the ending number will nort be print in the output thats why it is written like this
#     sum +=i
#     print("total sum=",sum) #for undersanding u do not include print ststement in for loop writr is seperately

# n=5
# sum=0
# for i in range(1,n+1):        #here n+1 is written because in range (stop section) always the ending number will nort be print in the output thats why it is written like this
#     sum +=i
# print("total sum=",sum)

# #..........................................................................

# #Q2)WAP to find the sum of first n natural numbers(using while)

# n=6
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("total sum=",sum)

# #..........................................................................

# #Q3)WAP to find the factorial of first n numbers (usinf for)

# n=5
# factorial=1 #we need to initialize by 1 for factorials if not ,,,u assign 0 dor it then the value multiply by 0 and the o/p will b 0 only
# for i in range(1,n+1):        #here n+1 is written because in range (stop section) always the ending number will nort be print in the output thats why it is written like this
#      factorial *=i
# print("total factorial value=",factorial)


# #............................................................................................................................................
# #Q4)WAP to find the factorial of first n numbers (using while)

# n=5
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print("factorial nalue is:",fact)    

# #Q5)WAP to find the factorial of first n numbers (using for)
# for x in range(6):
#   if(x==3): 
#    break
#   print(x)
# else:
#   print("Finally finished!")