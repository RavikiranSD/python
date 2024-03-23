# collection={1,2,3,4}
# print(collection)
# print(type(collection))

#now using duplicaate values in the sets
# collection={1,2,4,3,3,4}
# print(collection)
# print(type(collection))   #the duplicates are ignored as duplicates are not allowed in the sets

#We can even use the string values in the sets also
# collection={1,2,2,4,"hii","hello","hii"}
# print(collection)
# print(type(collection)) 
#in sets the O/P do not folllow the order .....it gives the output randomly without following any orderr

#printing total number of items:
# collection={1,2,2,4,"hii","hello","hii"}
# print(collection)
# print(len(collection)) #for printing the length / total items .....here also the duplicate numbers are ignored

#...........................................................................................................................

#creation of empty set::::

# col={}  #it is an syntax of empty dictionary
# print(type(col))

# #to printthe empty set
 
# col=set()
# print(type(col))

#=================================================================================================================================

#METHODS IN SETS::::

#1)set.add(el) : adds an element

# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(4)
# collection.add(2)
# collection.add(2)
# print(collection)  #O/P: {1, 2, 3,4} here also the duplicates ar ignored 

# ..............................................................
#2)set.remove(el): removes an element

# collection.remove(3)
# collection.remove(1)
# print(collection)  #O/P:{2, 4}

#if we want remone any value which is not present in the set then it gives O/P as:key error(and the given value)

# collection.remove(9)
# print(collection)  #O/P:KeyError: 9

# .............................................................................

#WE Can STORE any values in set (like tuples,string,float etc)

# collection=set()
# collection.add(3)
# collection.add(2)
# collection.add("Ravikiran")
# collection.add((1,2,3))
# print(collection)

#now try to add list in SET:

# collection.add([1,2,3]) 
# print(collection)   #WE cannot add lists in the sets
#                          #O/P as :  TypeError: unhashable type: 'list'

# ............................................................................................

#3)set.clear() : empties the set

# collection=set()
# collection.add(3)
# collection.add(2)
# collection.add("Ravikiran")
# collection.add((1,2,3))
# collection.clear()

#........................................................................
#4)set.pop()  :removes a random value

# collection={"hello","hii","python","coding","sql"}
# print(collection.pop())
# print(collection.pop())
# print(collection.pop())


#....................................................................................

#5)set.union(set2) :combines both set values and returns new

# set1={1,2,3,4}
# set2={3,4,5,6}
# print(set1)
# print(set2)
# print(set1.union(set2))  #for union set 
#                #output for union set..........O\P:{1,2,3,4,5,6} 
#                 #the duplicates are ignored 


#.................................................................................................

#6)set.intersection(set2)  : combines comman values and returns new

# set1={1,2,3,4}
# set2={3,4,5,6}
# print(set1.intersection(set2))




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#=============================================================================================================================
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++








# #PRACTICE QUESTIONS:::::::::::::::::

# #Q1)store the following meanings in python dictionary:
# #   table:"a piece of furniture","list of facts and figures"
# #   cat:"a small animal"

# dictionary={
#     "cat":"a small animal",
#     "table":["a piece of furniture","list of facts and figures"]  #you can store more than one values either in Lists or in Tuples
# }
# print(dictionary)


# # ----------------------------------------------------------------------------------------------------------------------------------------------------

# #Q2)you are given a list of subjects for students assume one classroom is required for 1 subject.How many classrooms are needed by all students.
# #    "python","java","c++","javascript","java","python","java","c++","c"

# subjects={
#     "python","java","c++","python","javascript","java","python","java","c++","c"
# }
# print(subjects)      #we got the individual unique subjets 
# print(len(subjects)) #total number of class room required

# #................................................................................................................................

# #Q3) WAP to enter marks of 3 subjects from user and store them in a dictionary.
# #Start with an empty dictionary and add one by one .Use subject name as key and marks value

# marks ={}
# x=int(input("enter Kannada marks:"))  #to add numbers we need to use int method in front of input method
# marks.update({"Kannada":x}) #for adding we use update method .....for updating the dictionary

# x=int(input("enter english marks:"))
# marks.update({"English":x})

# x=int(input("enter hindi marks:"))
# marks.update({"hindi":x})

# print(marks)

# #another way without using input method:
# marks={}
# marks["kannada"]=95
# marks["english"]=85
# marks["hind"]=88

# print(marks)

# # --------------------------------------------------------------------------------------------------------------------


# #Q4)Figure out a way to store 9 and 9.0 as seperate values i the set.
# #   (you can take help of built-in data types).

# # values={ 9 , 9.0}
# # print(values) #in python sets both the values of 9 and 9.0 consider them same only.
# #                 #if the float value has slight .25 also like ex: 9.25 then it shows the values differently
# # # O/P: {9}


# #another method:if we save 9.0 as string then it is possible to show both the values in output
# values={9,"9.0"}
# print(values)
#               #O/P:{9, '9.0'}

# #if we make 9 as string instead of 9.0 then,
# values={"9",9.0}
# print(values)
#              #O/P:{'9', 9.0}


# #another possible solution:using the builtin Data types,inthe values set and 
# #save them in two pairs using tuple and givind them the data type values
# values={
#     ("float",9.0),
#     ("int",9)
# }
# print(values)


