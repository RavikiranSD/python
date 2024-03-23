# IF Statement...

# a=20
# if(a>=20):
#     print("can vote")
#     print("can drive")
# ...................................................


# elif Statement.................



# a=20
# if(False):
#     print("can vote")
#     print("can drive")
# elif(True):
#     print("cannot")

#     a=20
# if(True):
#     print("can vote")
#     print("can drive")
# elif(False):
#     print("cannot")

#     ............................................
# light="green"

# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("walk")
# elif(light=="yellow"):
#     print("wait")
    
# print("end of code")    
#                          o/p... walk
#                                 end of code

# or "



# light="green" 
# if(light=="green"):
#     print("walk")
# elif(light=="green"):
#     print("stopk")
# elif(light=="yellow"):
#     print("wait")
    
# print("end of code")

# .................................................

# proof to show that the if ststement  will not go to the next statenmts even if the other ststements are true...

# num=5
# if(num>3):
#     print("true")
# elif(num>4):
#     print("true ans")

# ..........................................................

# ELSE Statement......

# light="blue"
# if(light=="green"):
#     print("walk")
# elif(light=="green"):
#     print("stopk")
# elif(light=="yellow"):
#     print("wait")
# else:
#     print("its broken")

#    (or)

# age=20
# if(age>=18):
#     print("can vote")
# else:
#     print("cant vote")

# ............................................................................... 

# mark=89
# if(mark>=90):
#     print("A grade")
# elif(mark>=80 and mark<90 ):
#     print("B Grade")
# elif(mark>=70 and mark<80):
#     print("C Grade")
# else:
#     print("D Grade")    

#     OR.......

# mark=8
# if(mark>=90):
#     grade="A"
# elif(mark>=80 and mark<90 ):
#      grade="B"
# elif(mark>=70 and mark<80):
#     grade="C"
# else:
#     grade="D"
# print("Marks of student -->",mark)
# print("Grade of student -->",grade)

# another method...........

# By using Input method..

# mark=input("Enter the marks")
# print("the result is",mark)
# if(mark>90):
#     print("A grade")
# elif(mark>80):
#     print("B Grade")
# elif(mark>70):
#     print("C Grade")
# else:
#     print("D Grade")   

# o/p: It shows invalid    
#  as in input methos whatever u enter the values it will take the values in Strings only ...but not takes in INT or FLOAT
# so to grt thr ans WE need to use The TYPE CASTING

# mark=int(input("Enter the marks"))
# print("Total marks are:",mark)
# if(mark>90):
#     print("A grade")
# elif(mark>80):
#     print("B Grade")
# elif(mark>70):
#     print("C Grade")
# else:
#     print("D Grade")   

# OR.........

# mark=int(input("Enter the Marks:"))
# if(mark>=90):
#     grade="A"
# elif(mark>=80 and mark<90 ):
#      grade="B"
# elif(mark>=70 and mark<80):
#     grade="C"
# else:
#     grade="D"
# print("Marks of student -->",mark)
# print("Grade of student -->",grade)


# ...........................................................................
# -------------------------------------------------------------------------

# NESTING Statement:-------------

# we can write the if tatement inside the if ststement which is completely valid  which is called Nesting Statement1

# age=30
# if(age>18):
#     print("Can Drive")
#     if(age>=75):
#         print("Cannot Drive")
# else:
#     print("Minor Cannot drive ")        

# OR..................////////////////////////////
   
# age=30
# if(age>18):
#     if(age>=75):
#         print("Cannot Drive")
#     elif(age>18):
#         print("can drive")
# else:
#     print("Minor Cannot drive ")    


 # by writing in proper format.........

# age=25
# if(age>=18):
#     if(age>75):
#         print("Cannor DRIVE")
#     else:    
#         print("can Drive")
# else:
#     print("Minor cannot DRIVE")


# -----------------------------------------------------------------
# ------------------------------------------------------------------

# Q1)WAP to check if a number entered by the user is odd or even

# a=int(input("Enter the number"))
# if(a%2==1):
#     print("given Value IS ODD")
# else:
#     print("Its EVEN Number")    

    # OR

# num=int(input("Enter the number"))
# rem=num%2
# if(rem==1):
#     print("given Value IS ODD")
# else:
#     print("Its EVEN Number") 

# ---------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------


# Q2)WAP to find the greatest of 3 number entered by the user?

# int(input("Enter the First Number"))
# b=int(input("Enter the Second Number"))
# c=int(input("Enter the Third Number"))

# if(a>=b and c<=b):
#     print("First is the Largest")
# elif(b>=c):
#     print("Second is the Largest")
# else:
#     print("Third is the LArgest")a=



# ------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

#  Q3)WAP to find the greatest of 4 number entered by the user?

# a=int(input("Enter the First Number"))
# b=int(input("Enter the Second Number"))
# c=int(input("Enter the Third Number"))
# d=int(input("Enter the Fourth Number"))

# if(a>=b and a>=d and a>=c):
#     print("First is the Largest")
# elif(b>=d and d>=c):
#     print("Second is the Largest")
# elif(c>=d):
#     print("Third is the LArgest")
# else:
#     print("Fourth is Largest")

# ---------------------------------------------------------------------
# -----------------------------------------------------------------------

# Q4)WAP to check if a munber is multiple of 7 or not?

# num=29
# if(num%7==0):
#     print("true")
# else:
#     print("False")


#    (OR)use input method.......

# num=int(input("Enter the number"))
# if(num%7==0):
#     print(num,"is multiple of 7")
# else:
#     print(num,"is Not a multiple of 7")


# --------------------------------------------------------------------
# ----------------------------------------------------------------------

# Q5)WAP to check if a munber is multiple of 5 or not?

# num=int(input("Enter the number"))
# if(num % 5 ==0):
#     print(num,"is multiple of 5")
# else:
#     print(num,"is Not a multiple of 5")