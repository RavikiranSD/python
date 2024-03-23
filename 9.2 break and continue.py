# #BREAK:used to terminate the loop when encountered.

# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1 
# print("end of loop")
# #when the i value becomes 3 the loop will stop automatically as the break statement is used
    
# #EX2:
# x=36
# nums=(1,4,9,16,25,36,49,64,81,36,100)
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("found ad index:",i )
#        #  break
#     else:
#         print("finding...")
#     i +=1
# print("end of loop")    
# #here after finfing its value it direectly come outside the the loop and the loop will stop as we have used the break statement
# #if the  break statement not used the loop will continue until the tuple ends .
    
# ##===============================================================================================================================================

# #CONTINUE:terminates execution inthe current iteration and continuos execution of the loop with the next iteration

# i=0
# while i<=5:
#     if(i==3): #here if i value becomes 3 we do not want  it to print so it skips that part as we used the CONTINUE statement for it so it willl increment it directly from IF STSTEMENT 
#         i+=1                          #and goes to the while part again and the provess goes on wntil the while condition completion
#         continue
#     print(i)
#     i+=1


# # #EX2:
# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         print("right")
#         continue         #skip
#     print(i)
#     i+=1



# # #EX3:if u want to print odd  numbers and skip even numbers
# i=1
# while i<=10:
#     if(i%2 == 0):
#         i+=1
#         continue  #if the value comes in even that time it gets  increment from the if statement ,
#     print(i)                  #and directly it goes to the while loop without printing the even values, as the if contain the CONTINUE statement
#     i+=1


# # #EX3:if u want to print even numbers and skip odd numbers
# i=1
# while i<=10:
#     if(i%2 == 1):
#         i+=1
#         continue  #if the value comes in odd that time it gets  increment from the if statement ,
#     print(i)                  #and directly it goes to the while loop without printing the odd values, as the if contain the CONTINUE statement
#     i+=1

       #(OR)another method for printing even numbers
# i=1
# while i<=10:
#     if(i%2 != 0):
#         i+=1
#         continue  #if the value comes in odd that time it gets  increment from the if statement ,
#     print(i)                  #and directly it goes to the while loop without printing the odd values, as the if contain the CONTINUE statement
#     i+=1

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")