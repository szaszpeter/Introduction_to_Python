# Introduction to Python

A repo containing a Python cheat sheat and a series of sample scripts.

## Navigating and Working with Files

- `cd` - change directory
- `ls` - list files, see list of options
- `touch` - create a file 
- `nano` - edit file
- `cp <origin> <destination>` - copy
- `mv <origin> <destination>` - move
- `rm <filename>` - remove
- `mkdir` - create directory
- `rmdir` - remove directory
- `cat` - display content of a file

## Install Python

## Numbers

- basic operators
- division
- modulus
- variables

## Strings

- basic strings
- `""` marks and `''` marks
- `\` escape characters
- special characters: `\n` = newline
- `print()` function
- `print(r"string")` - print raw string ignoring special characters
- mathematical operations on strings: 
 		- addition of two strings 
 		- multiplication with numbers


## Slicing Up Strings

- declare string variable `var`
- `var[0]` - index of first character
- `var[-1]` - index of last character
- `var[m:n]` - substring starting from index m, ending on index n
- `var[:n]` - substring starting from index 0, ending on index n
- `var[:]` - substring containing all the indexes
- `len(var)` - length of string variable `var`

## Lists

- declare a list variable called `list`
- `list[n]` - returns element at index `n`
- `list[:]` - returns all elements
- `list[m:n]` - returns a sublist starting at index m, ending at index n
- `list + [0,1,2]` - temporarily adds 0,1,2 elements to the list
- `list.append(1)` - adds 1 as a new element to the list
- `list[:2] = [0,0]` - replaces the first 2 elements with 0 
- `list[:] = []` - deletes all the elements from the list


## if elif else Conditions

      if <condition>:
  	    // execute code
      elif <condition>:
	      // execute code
	   else:
	      // execute else branch

## For Loop

- declare an list called 'list'
- `for i in list:`
- `for i in list[:n]` <- this will only execute code for the first n elements of the list


## Comments and break:

- `#` comment a single line
- `''' ... '''` comment out a whole block of lines
- `break` - breaks a for loop
- `continue` - skips the execution of a for loop to the next block

## Functions

- define a function with the following syntax:

	`def function():`
  
	`def function(var):` <- var is a variable which can be passed when calling the function
		
## Return Values

- define a function with the following syntax:

	  def function():
	    // code to execute
	    return <value>

## Default Values for Arguments

- define a function with the following syntax:

	`def function(var = 'default value'):`  <'default value' is the default value used if nothing is passed into the function

## Variable scopes

- variables defined in functions are only available inside the function
- variables defined at script level are available only if they are declared above the functions execution line.

## Keyword Arguments

- define a function with the following syntax:

	`def function(keyword1 = "default_value1", keyword2 = "default_value2")`

- now when calling the function, one can specify the keyword

	`function(keyword2="custom_value")` <- this allows us to call functions with only a part of it's arguments instead of all of them. By mentioning the keyword we can directly specify which one of the arguments we are passing in.

## Flexible Number of Arguments

- define a function with the following syntax:

	`def function(*args):`

- now when calling the function, one can specify as many arguments one wants.

	    function(1,2)
  	    function(1,2,3)
	    function(1,2,3,4,5)
	
  etc.

## Unpacking Arguments

- define a function with the following syntax:

	`def function(arg1, arg2, arg3):`

- define a list with three elements: `list = [1,2,3]`

- now when calling the function, pass the list as argument

	`function(*list)` <- the * sign will automatically unpack the elements of the list. 

- Warning: If the list has more elements than expected by the function, an exception will be thrown at runtime.

- `*` can be used as well for unpacking a previously unknown number of elements

  `first, *middle, last = [1, 2, 3, 4, 5, 6, 7]`

- the above code will produce the following result: `first = 1, last = 7, middle = [2,3,4,5,6]`

## Sets

- define a set with the following syntax:

	`set = {val1, val2, val3, val4}`

- check if an element is part of a set:

	`if element in set: -> return true or false` 

- Cool Fact: sets can contain different types of elements

	`rainbow_set = {"string1", 1, "string2",2, etc....}`

## Dictionaries

- define a dictionary with the following syntax:

	`dictionary = {"key1":"value1", "key2":"value2"}`

- iterate through the items of a dictionary:

	    for k,v in dictionary.items():
		    // execute code
		    // execute code

## Modules

- when defining a new script, one can import other modules / python scripts in order to access some of it's content

	`import <module_name>`

	`<module_name>.<function_name>` <- this line will execute the function called <function_name>

- Fun Facts: Whenever a module is imported all the code inside of it gets executed!

## Exceptions

- to handle exceptions use the try - except blocks

	    try:
		    //execute code
	    except <SpecificErrorName>:
		    // handle a specific error case
	    except:
		    // handle generic uncaught errors
	    finally:
		    // this will run in every case 


## Classes and objects

- define classes with class keyword

	    class SomeClass:

		    def someFunction(self):
			    // some code here

- instantiate a class by calling the classname with () 

	`variable = SomeClass()`

- call methods from the class

	`variable.someFunction()`


## Init functions

- init functions are blocks of code that get executed when their parent class is instantiated

	    def __init__(self):
		    // some code here

- positional arguments can be passed into the init function, which makes them as mandatory class arguments when instantiating

	    class SomeClass:
		    def __init__(self, someVariable):
			    // some code here

	`object = SomeClass(someVariable)` <- in this case someVariable is mandatory and it will be a global variable inside SomeClass




## Inheritance and Multiple Inheritance

	    Class1()
		    // class code here

	    Class2()
		    // class code here

	    Class3(Class1, Class2)
		    pass

- in this above example Class3 is inheriting from Class1, Class2.
- the pass keyword is to avoid compiler error requiring indented block of code after class declaration
- instead of pass, there could go actual class implementation

## Threading

- to access the threading library, import it.

	`import threading`

- define a class that is inheriting from threading.Thread

	    class Example(threading.Thread)

		    def run(self):
			    // execute code

- call the start method of the newly created class to invoke the run method

	    object = Example()
	    object.start() 

## Zip

- combining the values of two lists

	    a = [1,2,3]
	    b = [a,b,c]

	    zip(a,b) 

- this code will produce a new list of tuples => `['1,a', '2,b', '3,c']`

## Lambda

- small nameless functions 

	`variable = lambda x: x*3`

## Pack / Unpack data

- pack data into bytes format

	`pack('<format>', * <values>) `

- unpack data from bytes format

	`unpack('<format>', <bytes>)`













