# while True:
#     print("hii")   #in while loop if the condition is true the loop coes on continueing infinitely
#                    #so u need to put the conditions for it and thhe increment decrement conditions also
    

# count=1
# while count <=5 :
#     print("ravi")
#     count +=1
#     print("loop ended")     #dont write the last print statement long with the loop ....it considers also the loop and prints it again and again.....write it saperetely
 
# #  O/P:
# # ravi
# # loop ended
# # ravi
# # loop ended
# # ravi
# # loop ended
# # ravi
# # loop ended
# # ravi
# # loop ended

# count=1
# while count <=5 :
#     print("ravi")
#     count +=1

# print("loop ended")    
# # O/P:
# # ravi
# # ravi
# # ravi
# # ravi
# # ravi
# # loop ended

#...........................................................................
#to get the total count of the loop:

# i=1
# while i<=5:
#     print("hii")
#     i+=1
# print(i)    

# #(OR)

# i=1
# while i<=5:
#      print("hii",i)
#      i+=1

# #(OR)

# i=1
# while i<=5:
#      print(i)
#      i+=1

# #...............................................................................................

# #REVERSE THE LOOP:
# i=5
# while i>=1:
#     print("hii")
#     i-=1
# #(OR)
# i=5
# while i>=1:
#     print(i)
#     i-=1


# #................................................................................................

# #infinite loop: (there is no practical use of infinite loops,so it may crash ur code also) 
# i=5
# while i<=6:
#     print(i)
#     i-=1

# #............................................................................................................................

# #Q1)print numbers from 1 to 100
# i=1        #initilization:which means the value which we have started
# while i<=100:      #condition
#     print(i)
#     i+=1           #updation
# print("code executed")

# #........................................................................................................

# #Q2) print numbers from 100 to 1

# i=100
# while i>=1:     #stopping condition
#     print(i)
#     i-=1
# print("code end")   

# #.............................................................................................

# #Q3) print the multiplication table of a number n

# #to get the multiplication table
# i=1
# while i<=10:
#     print(5*i)
#     i+=1

# #now by using the user input method:
# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# #to get the total count:
# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(i,n*i)
#     i+=1

# #.............................................................................................

# #Q4)print the elements of the following list using a loop:
# #   [1,4,9,16,25,36,49,64,81,100]
  
# nums=[1,4,9,16,25,36,49,64,81,100]
# index=0           #initilization:which means the value which we have started
# while index<len(nums):
#     print(nums[index])
#     index+=1
# #traverse: whenever we r going means like treverse or travelling every item of the list or tuple  through wich we may perfoorm amny action on that elenent or simply printing it is called as traversing.
    
#     #other example::::
# heros=["thor","ironman","batman","superman"]
# i=0
# while i<len(heros):
#     print(heros[i])
#     i+=1


# #.............................................................................................................................................

# #Q5)search for number x in this tuple using loop:
#     # (1,4,9,16,25,36,49,64,81,100)

# x=36
# nums=(1,4,9,16,25,36,49,64,81,100)
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("found ad index:",i )
#     i +=1
# #O/P: found ad index: 5

#    #.................................. 
#     #if u want to find how it works ....then take another example of of tuple having same value twice in it and see how it works

# x=36
# nums=(1,4,9,16,25,36,49,64,81,100)
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("found ad index:",i )
#     else:
#         print("finding....")
#     i +=1

#     #here in the output it showes finding every time untli the given value get in the tuple ,, if it get the value then it shows other vise it goes on showind up to its size
#     #ex:noe we are having the same value now we se what will b the output is:
# x=36
# nums=(1,4,9,16,25,36,49,64,81,36,100)
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("found ad index:",i )
#     else:
#         print("finding...")
#     i +=1
