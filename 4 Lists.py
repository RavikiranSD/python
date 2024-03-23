# marks1=78.5
# marks2=55.3
# marks3=48.4
# marks4=44
# marks5=59.1

# easy method.....
# use the list method to store multiple values .....

# marks=[78.5,55.3,48.4,44,59.1]
# print(marks)

# print(type(marks)) #......to show which Type it is 

# print(marks[1])   #...............Accessing a particular element of INDEX in a LIST

# print(len(marks))  #.............LENGTH of the LIST


# ...........................................................................
# in python we can store the diff. type of DATA TYPES values in a single LIST

# student=["RAVI",24,"Kalaburagi",8.23]
# print(student)

# STRING and PYTHON LIST are mostly similar...........but there is a major difference between them
#  the STRIMGS are IMMUTABLE in python(accessing of values in index is allowed,but changing(mutate) that value ti another is not allowed )
#  the LISTS are MUTABLE in python(both ACCESSING and CHANGING is allowen in python)

# ex:string
# str="hello"
# print(str[0])
# print[0]="y"  #o/p: object doesnot support item assignment
#                it means strings are IMMUTABLE

# ex:list

# student=["RAVI",24,"Kalaburagi",8.23]
# print(student[2])  #printing the particular index of list(we can directlu write the changong part, but this line is written just for understanding)
# student[2]="BENGALURU"   #changing the index value to new one
# print(student)

# O/P:.. kalaburagi
#        ['ravi',24,'bengaluru',8.23]

# ............................................................................................

# if we made a list contain 4 indices as 0,1,2,3 and if we try to access the 5th index then ot compiler will shoe the erroe....as the limit of the list is 4 

# ex:
# student=["RAVI",24,"Kalaburagi",8.23]
# print(student[5]) 
#  o/p: list index out of range


# ------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


# LIST SLICING:::::::::::::::

# marks=[85,94,76.9,43.4,65]
# print(marks[0:4]) 
# #(OR)
# print(marks[:4])

# print(marks[1:4]) 
# #(OR)
# print(marks[1:]) 

# #negative list slicing is also available....
# print(marks[-3:-1])


# ===============================================================================================================
# -----------------------------------------------------------------------------------------------

# LIST METHODS:::::::::::::::::::::::::::::::::

# *generally the strings methods used to return the new updated string values,
#        but these list methods gives NONE as they do nat have any values to return.

# 1) APPEND METHOD: adds one element at he end(we can also called mutatinf the list or changing the list)

# #ex1:
# list =[24,45,56,67]
# list.append(78)
# print(list)

# #ex2:
# list =[24,"a",56,"dd",]
# list.append("hiii")
# print(list)

# list.append() do not give any return when we print .....it just gives NONE as Output
# list =[24,45,56,67]
# print(list.append())
# (OR)......even assigining value also output will b same ....NONE
# print(list.append(78))


# ------------------------------------------------------------------------------------------------

# 2)SORT METHOD:sorts in assending order

# ex1:
# list =[24,45,56,67]
# list.sort()
# print(list)

# ex2:
# list.sort() do not give any return when we print .....it just gives NONE as Output
# list =[24,45,56,67]
# print(list.sort())
# O/P: NONE

# ex3:
# lists=['a','b','f','g']
# lists.sort()
# print(lists)

# ex4:
# lists=["mango","pineaple","apple","banana"]
# lists.sort()
# print(lists)

# ----------------------------------------------------------------------------------------

# 3)SORT METHOD(DESCENDING):sorts in descendinfg order ....just need to use the syntax as   list.sort(reverse=True)

# ex1:
# list =[24,45,56,67]
# list.sort(reverse=True) #here in the TRUE,"T" must b always in capital letter.
# print(list)

# ex2:
# lists=['a','b','f','g']
# lists.sort(reverse=True)
# print(lists)

# ex3:
# lists=["mango","pineaple","apple","banana"]
# lists.sort(reverse=True)
# print(lists)

# Here the strings CHARACTER ,which it sees in alphabitical order

# ----------------------------------------------------------------------------------------------------------------------

# 4)REVERSE LIST:it reverses the values in the list from first to last ,to last to first.

# ex1:
# a=[3,5,1,5,9]
# a.reverse()
# print(a)

# ex2:
# a=['f','a','e','b']
# a.reverse()
# print(a)

# ---------------------------------------------------------------------------------------------------------------------

# 5)INSERT METHOD:it is very similar to append,like if there is a list and we want to add the avlue in the middle if the list then we can do with this method.

# ex1:
# list=[7,5,1,5,9]
# list.insert(0,4)
# print(list)  #here  whichever the value u want to insert them it will show first at he place u assigned for it and remaining values will show accordingly
#               and we have not replaced the value here,we just inserting the value to that locaton only 


# ex2:
# list=['f','a','e','b']
# list.insert(1,'z')   
# print(list)

# ---------------------------------------------------------------------------------------------------------------

# 6)REMOVE METHOD:Removes first occurance of element  means if we want to remove any value it searches in the list annd removes the value which firstly it sees
 
# EX1:
# list=[7,5,1,5,9]
# list.remove(5)
# print(list)

# EX2:
# list=['f','a','e','b']
# list.remove('a')
# print(list)

# -----------------------------------------------------------------------------------------------------------

# 7)POP METHOD:removes element at any particular INDEX.       
           # And if u do not specify the index,the pop() method removes the last item.
# Ex1:
# list=[7,5,1,3,4,6,9]
# list.pop(2)
# print(list)


# ---------------------------------------------------------------------------------------------------------------------

#8)EXTEND LIST:

# list1=[2,4,6,8]
# list2=[23,56,48]
# list1.extend(list2)
# print(list1)

# --------------------------------------------------------------------------------------------

#9)COPY METHOD:
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().

#ex1)

# list1=[1,2,3,6,8,4]
# list2=list1.copy()
# print(list2)

#ex2)

# list1 = ["apple", "banana", "cherry"]
# list2 = list1.copy()
# print(list2)


# -----------------------------------------------------------------------------------------
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x.upper() for x in fruits]

# print(newlist)


# ------------------------------------------------------------------------------------------

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)