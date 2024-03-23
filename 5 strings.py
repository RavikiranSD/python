# adding strings

# a= "apna"
# b="collrge"
# print (a+b)

    # or

# a= "apna"
# b="collrge"
# result =a+b 
# print (result)

# a= "apna"
# b="collrge"
# result =a+" "+b #for giving space used inverted commas
# print (result)
# ......................................................

#length of string....
# a= "apna"
# b="collrge"
# result =a+b 
# print (result)
# print(len(result))

# ............................................................

# how to let go the single  line to next line

# str1="Avul Pakir Jainulabdeen Abdul Kalam BR was an Indian aerospace scientist and statesman"
# print(str1)

# to change the line use  \n for it.

# str1="Avul Pakir Jainulabdeen Abdul Kalam BR \n an Indian aerospace scientist and statesman"
# print(str1)

# .............................................................................

#  Indexing

# str = "Apna College"
# ch=str[0]
# print(ch)

              # or

# str="Apna college"
# print(str[3])
 
# we can access characters in INDEX form But we cannot Manuplate/ Modify it(we cannot replace it with other characters in that present ones....) 
# (string doesnot support item assignment)

# ......................................................................................

# Slicing Of Strings........

# a="Ravikiran"
# print(a[0:4]) 

#  or

# print(a[:4])  #it is ok if we do nor write 0 in starting index
# print(a[4:9])

# or

# print(a[4:len(a)])  #we can write length of the index also to for the Last Index..

# ......................................................................


# SLICING (Negative Index)----------

# a="Apple"
# print(a[-5:-2])
# print(a[-4:len(a)])
# print(a[-5:4])   

# .-----------------------------------------------------------------------------


# STRING Functions--------------------

# Endswith....
# str="hi im Ravi Stydying Python"
# print(str.endswith("hon"))
# print(str.endswith("py"))
# print(str.endswith("im"))

# Capatilize.......

# str="hi im Ravi Stydying Python"
# print(str.capitalize()) #whenever we try to modify string like this we will nor modify the original string instead it will create a new string...and no changes made in the old strings
# print(str)
# ..............................
#to modify the value in the original string shown down..
# str="hi im Ravi Stydying Python"
# str=print(str.capitalize())
# print(str)
# here the new value which is returning will be storing in the old variable itself..
# when we print it we can see that ..the modifications have been made in the original strings itself..

# ..........................................................................

# REPLACE Function..........

# a="hi im Ravi Studying Python"
# print(a.replace("o","5")) 
# print(a.replace("Python","HTML5"))

# ..................................................................

#Find Function......

# a="hi im Ravi Studying Python"
# print(a.find("hi")) #it starts from the 0th index 
# print(a.find("Ravi"))# it starts from the 6th indec
# print(a.find("kiran"))
#kiran is not available in this ...so it shows -1 as it is not an valid index
# negative index exists only for SLICING

# .............................................................................

# COUNT Function....
# a="hi im Ravi Studying Python"
# print(a.count("o"))
# print(a.count("i"))

# .....................................................................

# Q1) WAP to input users first name and print its length?
# a=("Ravikiran")
# print(a[0:len(a)])..........Wrong Ans. code Attempted

# e=input ("enter your name:")
# print("your name length is", len(e))

# ...............................................................

# Q2) WAP to find the occurance of '$' in a string?

# a=("im a studen$ lear$ the code$g")
# print(a.count("$"))

# ........................................................................

