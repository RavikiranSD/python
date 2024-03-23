# # 1)
# tup=()
# print(tup)
# print(type(tup))

# # 2)
# tup=("true",)
# print(tup)
# print(type(tup))
# #both the above 1 and2 are tuples
# #use the comma[,] even for the single value it is cumpolsary for the tuples otherwise it thinks it as an integer,float,or the string whichever it is written in the COMMON BRackets.
# # both lists and tuple are same in many aspectes ....to identify them for tuples we need to write them in the common brackets and for liste write in the square brakets
# #Example no.3 and no.4, shows as it is a string,INTEGER as the output

# # 3)
# tup=("true")
# print(tup)
# print(type(tup))

# # 4)
# tup=(5)
# print(tup)
# print(type(tup))

# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------

# #TUPLE SLICING:
# # slicing in tuple works as same as the lists
# tup=(1,2,3,4,)
# print(tup[1:3])

# ==============================================================================================================================

# TUPLE METHOD::::

# 1)INDEX METHOD:returns index of first occurance

# tup=(1,2,3,4)
# print(tup.index(2))
# #here the output 1 is INDEX ...........and the 2 which is written in the print statement is the ELEMENT which we wanted to search for..

# tup=(3,2,6,4,8,1)
# print(tup.index(3))

# ------------------------------------------------------------------------------------------------------------------------

#2)count METHOD::counts total occurance
          #here whichever the element we pass ,which shows that element how many times it existed in that TUPLE comen the total count of it.

# # tup=(3,2,6,4,8,1)
# # print(tup.count(3))
#    #here the O/P shows 1 as 3 exist only 1 in the given tuple

# tup=(3,4,2,6,4,8,1)
# print(tup.count(4))

# # the o/p is 2 as the given tuplle has TWO 4's in it.


# =======================================================================================================================================
# ==================================================================================================================================================

##Q1)WAP to ask the user to enter the names of their 3 favourate movies & store them in a list.

# list=[]
# a=input("enter 1st movie:")
# b=input("enter 2nd movie:")
# c=input("enter 3rd movie:")

# list.append(a)
# list.append(b)
# list.append(c)
# print(list)

##(OR)----------------

##instead of making 3 different variables we can make same varilable for all  3 for assigning the values.
# list=[]
# a=input("enter 1st movie:")
# list.append(a)
# a=input("enter 2nd movie:")
# list.append(a)
# a=input("enter 3rd movie:")
# list.append(a)

# print(list)

##(OR)----------------

##we can APPEND directly,which mean instead of writing the variablle name(a) we can write the list with le append and writing the input variable in theappend method itself. 

# list=[]
# list.append(input("enter 1st movie:"))
# list.append(input("enter 2nd movie:"))
# list.append(input("enter 3rd movie:"))
# print(list)

## ===========================================================================================================================================================
## ======================================================================================================================================================

# #Q2)WAP to check if a list contain a palindrome of elements.(Hinf: use copy() method) 

# list1=[1,2,3,2,1]

# list2=list1.copy()
# list2.reverse()
# print(list2)
# if(list1==list2):
#     print("its a palindrome")
# else:
#     print("its not palindrome")


## (OR)by using input method

# list1=[]
# list1=[input("enter the values:")]
# list2=[input(list1.copy())]
# list2.reverse                                          #not able to solve the problem
# if(list1==list2):
#     print("it is a palindrome")
# else:
#     print("it is not a Palindrome")    


#-------------------------------------------------------------------------------------------------


# #Q3)WAP to count the number of students with the "A" grade in the following tuple.
#        #("C","D","A","A","B","B","A")

# grade=("C","D","A","A","B","B","A")
# aa=grade.count("A")
# print(aa)

# #(OR)  .......the easy method...

# grade=("C","D","A","A","B","B","A")
# print(grade.count("A"))


# --------------------------------------------------------------------------------------------------------------------------

# #Q4)store the above values in a list and sort them from "A"to"D".
  
# grade=["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)