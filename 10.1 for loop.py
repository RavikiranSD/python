# nums=[1,2,3,4,5,6,7]
# for val in nums:
#     print(val)

# #here value refers to variavle 
# # we can use for loop in tuple also
# tup=(1,2,3,4,5,6,7)
# for num in tup:      #here num is variable
#     print(val)

# #...........................................................        
# veggie=["tomato","cucumber","onion","brinjal"] 
# for i in veggie:
#     print(i)   
# #here i refers to variable


# #generally if there is an iterator on which we are working on,means like we have a variable which we are updating 
# #(or)if we have any stoping condition that timt we use while loops 
# #and if we have to traverse the data types,lists ,string all that work is done with the for loop

# #by using the string:
# str="ravikiran"
# for char in str:
#     print(char) #here char is the variable

# #........................................................................................

# #whenever we are using the for loop or while loop with that we can use  ELSE its completely optional and not cumpolsary
# #we use else for those specific cases where we use the BREAK

#ex1: 
# nums=[1,2,3,4,5,6,7]
# for val in nums:
#     print(val)
# else:
#     print("END")

# #ex2:
# str="ravikiran"
# for char in str:
#     if(char=='v'):
#         print("v found")
#     print(char)
# else:
#     print("END")
# #O/P:
# #r
# #a
# #v found
# #v
# #i
# #k
# #i
# #r
# #a
# #n
# #END       

# #now bu using the break statement:
# str="ravikiran"
# for char in str:
#     if(char=='v'):
#         print("v found")
#         break         #here in if statement we hit he condition so after that the code ended as it hit the break ,and ELSE part didnt executed ,
#                         #and if u want to print the else statement in this code then remove it ,then the remainind END statement will also print 
#     # print(char)  
# else:
#     print("END")

# #O/P:
# #r
# #a
# #v found    
    

# #............................................
#     #now ask a char which is not presenrt in the string
# str="ravikiran"
# for char in str:
#     if(char=='z'):
#         print("l found")
#         break
#     # print(char)       #if we print this statement then it will give the whole output and do not show whwther the new asked character is present or not
#                         #even if the asked char not present then also it will give the same o/p only ,,so if we do not writ this then we can know it is present in it or not ,if not present then ELSE statement hits directly    
# else:
#     print("NOT FOUNDEND")        

# #O/P: NOT FOUNDEND
    
# #...................................................................................................................................................................................................

# #Q1)print the elements of the followinf list using a loop
# # [1,4,9,16,25,36,49,64,81,100]

# nums=[1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)

##.......................................................................
## search for a number x in this tuple using loop:
## [1,4,9,16,25,36,49,64,81,100]


# nums=(1,4,9,16,25,36,49,64,81,100,9)
# x=9

# idx=0
# for el in nums:
#     if(el==x):
#       print("number found at idx",idx)
#     idx += 1

# #O/P:
# # number found at idx 2
# # number found at idx 10

# #if u want only one index to print simply use BREAK in the code like below
# nums=(1,4,9,16,25,36,49,64,81,100,9)
# x=9

# idx=0
# for el in nums:
#     if(el==x):
#       print("number found at idx",idx)
#       break
#     idx += 1 
# #O/P:number found at idx 2

















# .................................not getting o/p in 
# num=tuple([1,4,9,16,25,36,49,64,81,100])
# # print(num)

# x=4
# idx=0
# x=input("enter the number:")
# for ele in num:
#     if(ele==x):                      #not getting correct output ,missing something,,,,,,,,,refer thr below code it is correct one
#      print("yes exist",idx)
#      idx+=1
#     break
    
# else:
#    print(idx,"do not exist") 

#...................................................................
#the correct code by using input method:


# # Define the tuple
# numbers = tuple([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

# # Get input from the user
# x = int(input("Enter the number to search for: "))

# # Initialize the index variable
# idx = 0

# # Iterate through the tuple
# for ele in numbers:
#     if ele == x:
#         print("Yes, it exists at index:", idx)
#         break
#     idx += 1
# else:
#     print("Does not exist in the tuple.")