# dict={
#     "name":"ravikiran",
#     "sub":["python","c","java"],   #you can store in tuple form or list form
#     "topics" :("dict","set"),
#     "age":35,
#     "is_adult": True,
#     12.99 : 94.34
# }
# print(dict)

# #...........................................................................

# #if we want to access the values

# #ex:
# print(dict["age"])
# print(dict["is_adult"])
# print(dict[12.99])
# print(dict["sub"])

# #if we write any ky which is nor present in the dictionary it shows the erroe as shown below

# print(dict["surname"])

# #O/P:  print(dict["surname"])
#  #         ~~~~^^^^^^^^^^^
# #KeyError: 'surname'

## ..........................................................................................................

## if we want to change the value and assign any new values ....we can do that also

# #Ex:

# dict["name"]="SUNIL"
# print(dict)

# #We can even add a new value also
# dict["L name"]="SD"
# print(dict)

# #now here we can that the dictionaries in python are mutable
# #we cannot assign values to the same key ......if we do like thet it simply OVERWRITE THE VALUES instead of showing different values

# dict["name"]=24
# print(dict)

# #here the new value has assigned to a same key to show both dofferently but instesd it has OVERWRITE that value

# #......................................................................................................................

# #we can create an empty dictionary also
# #EX:
# null_dict={}
# print(null_dict)

# #we can even add values in the bnull dictionaries also

# null_dict["name"]="Abhi"
# print(null_dict)

# #===========================================================================================================================

# #NESTED DICTIONARIES:::::
 
# student={
#     "name":"vilas",
#     "subjects": {
#         "phy":75,
#         "chem":56,
#         "math":84
#     },
#     "result":"pass"
# }
# print(student)

# #we can also print only the SUBJECTS part also
# print(student["subjects"])

# #and can print only the MARKS also
# print(student["subjects"]["math"])

# #whenever if the data is available in the nested format then ....we can get the RELEVENT INFORMATION/DATA by placing square brackets on one beside another ..


# #=====================================================================================================================================================================
# #==============================================================================================================================================================================

# #DICTIONARY METHODS::

# #EX:
# info={
#     "name":"ravikiran",
#     "sub":["python","c","java"],
#     "topics" :("dict","set"),
#     "age":35,
#     "is_adult": True,
#     12.99 : 94.34
# }

# #EX2:

# student={
#     "name":"vilas",
#     "subjects": {
#         "phy":75,
#         "chem":56,
#         "math":84
#     },
#     "result":"pass"
# }

# #1) keys ():return all keys

# print(info.keys())
# print(student.keys())
# #in O/P it shows as dict_keys[and all key values in list format]
# #the nested keys do not return only the outer line keys returns
# #                  .......................
# #we can convert that data type of dict_keys ........can be converted into normal lists (or)tuple
# #by using type casting

# #in list form.......
# print(list(info.keys()))
# print(list(student.keys()))

# #in tuple form.....
# print(tuple(info.keys()))
# print(tuple(student.keys()))

# #we can fetch the ttal no.fo the keys also
# print(len(info.keys()))

# #or we can get thr length of the list also
# print(len(list(info.keys())))

# #=================================================================================================================

# #2)value ():return all values
# print(info.values())
# print(student.values())
# #...........................they can also b stored in list
# print(list(student.values()))
# print(list(info.values()))

# #==================================================================================================

# #3)item method():returns all(key,value)pairs as tuples
# print(student.items())
# print(info.items())

# #below written in list format ......
# print(list(student.items()))
# print(list(info.items()))

# #we can access them individually also
# pairs=list(student.items())
# print(pairs)
# print(pairs[0]) #if u want to access its first pair 
# print(pairs[2]) #if u want to access its third pair 
                               
# aa=list(info.items())
# print(aa[1])
# print(aa[3])

# #=======================================================================================================================

# #4)get():returns the key according to value

# #now we have 2 methods to get the vlues of the key  they are

# print(student["name"])
# print(student.get("name"))
# #both show the same O/P.....

# #print(student["name2"])              #o/p:ERROR
# #print(student.get("name2"))        #o/p: none
# #but whenever if we tried any new key  which is not present in the dictionary
# #then the first method simply shows the ERROR
# #the second method i.e, get() dhows NONE in the O/P if the information is not available in the dictioary


# ==========================================================================================================================================

# # 5)update():inserts the specified items to the dictionary

# newdict={"city":"kalaburagi"}
# student.update(newdict)
# print(student)
        # #OR
# student.update({"city":"kalaburagi"})
# print(student)

## you can keep multiple key values also
# student.update({"city":"kalaburagi","pin":123654})
# print(student)

# #if u updated any new value in the old  key of the dictionary then in o/p the value gets OVERWRITE to the new one 
# #(because in DIICTINARIES the DUPLICATE KEYS are NOT allowed)
# student.update({"name":"vishwa","pin":123654})
# print(student)#the value of name has been over written 



