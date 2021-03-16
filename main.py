
##########################################################################################################
"""*args and **kwargs

    https://www.geeksforgeeks.org/args-kwargs-python/#:~:text=The%20special%20syntax%20**kwargs,and%20any%20number%20of%20them).
"""
def myFun(*args,**kwargs): 
	print("args: ", args) 
	print("kwargs: ", kwargs) 


# Now we can use both *args ,**kwargs 
# to pass arguments to this function : 
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks") 

##########################################################################################################
"""python dictionaries
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Python3 Program to check whether a 
# given key already exists in a dictionary. 

# Function to print sum 
def checkKey(dict, key): 
	
	if key in dict.keys(): 
		print("Present, ", end =" ") 
		print("value =", dict[key]) 
	else: 
		print("Not present") 

# Driver Code 
dict = {'a': 100, 'b':200, 'c':300} 

key = 'b'
checkKey(dict, key) 

key = 'w'
checkKey(dict, key) 

# Python3 Program to check whether a 
# given key already exists in a dictionary. 

# Function to print sum 
def checkKey(dict, key): 
	
	if dict.has_key(key): 
		print "Present, value =", dict[key] 
	else: 
		print "Not present"

# Driver Function 
dict = {'a': 100, 'b':200, 'c':300} 
key = 'b'
checkKey(dict, key) 

key = 'w'
checkKey(dict, key) 


# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(a, b, c):
	print(a, b, c)

# A call with unpacking of dictionary
d = {'a':2, 'b':4, 'c':10}
fun(**d)


##########################################################################################################


 
