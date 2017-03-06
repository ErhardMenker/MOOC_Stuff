###Chapter 4: Functions###

	##Function Calls
		#In programming, a 'function' is a named sequence of statments that performs a computation.
		#Definining a function requires specifying:
			#its 'name'
			#its sequence of statements
		#When a defined function needs to be executed and is referred to by exact name in the program, it is 'called'.
		#A function returns the appropriate 'return value' based on the inputted 'function argument'.
			type(32) #returns 'int'
			#the 'type' function returns the corresponding output value of the expression in parenthesis, mapping '32' to its Python type, 'int'.

	##Built-in Functions
		#Python provides a number of important built-in functions that performs standard operations.
		#Built-in functions means that the relationship between input and output do not need to be defined.
		#Popular built-in functions include:
			max('Hello world') ##returns 'w' , or the 'largest character' in the inputted string
			min('Hello world') ##returns ' ', or the 'smallest character' in the inputted string
			len('Hello world') ##returns 11, or the number of characters in the inputted string
		#Built-in functions should not be used as variable names, to avoid syntactic confusion.
		
	##Type Conversion Functions
		#Type conversion functions convert values from one type to another if possible...
		#...If type conversion is not possible, an error occurs.
		#str, int, and float functions convert inputted parameters into strings, integers, and floats, respectively.
			float(32) #converts integer '32' into float 32.0
			int('Hello') #non-sensical coercion; it is impossible to convert string 'hello' into a float
			int(3.99999) #converts floating-point value to an integer by removing any decimal points in the float's value
			float('3.14159') #convert string '3.14159' to float 3.14159
			str(32) #converts integer 32 into string '32'.
			
	##Random Numbers
		#An 'algorithm' is a general process for solving a category of problems.
		#'Deterministic' means that given equal inputs, computer programs should return the same output.
		#For programs encapturing randomness, algorithms should be used that generate 'pseudorandom numbers' as inputs...
		#...'pseudorandom' means that the numbers are generated by deterministic computation which should appear random by naive inspection.
		#The 'random module' ,when imported, provides tools for generating random numbers by using different parameters/distributions:
		#To access a function from an imported module, the notation is typically module_name.functionname()...
		#...specifying module_name.function_name() is called 'dot notation'.
				import random
				for i in range(10) :
					x = random.random()
					print (x) #prints 10 random numbers uniformly distributed on [0,1)
			#Calling 'random.randint(<a>,<b>) returns an integer uniformly on [a,b].
				import random
				random.randint(6, 10) ##returns 6, 7, 8, 9, or 10 with probability 20%, each
			#Calling 'random.choice(t)' from a sequence 't' returns an element of the list with equal probability.
				t = [1, 2, 3]
				import random
				random.choice(t) #returns 1, 2, or 3 with probability one-third for each
		#Naively calling for random number generation multiple times will not generate the same random numbers without setting the 'seed'.
		#The random module provides options to generate RVs from other distributions such as Gaussian, exponential, gamma, etc
		
	##Math Functions
		#Importing the 'math module' allows usage of fundamental math functions.
		#By 'dot notation' , math.function_name must be called to cite the function.
			import math
			ratio = signal_power / noise_power
			decibels = 10 * math.log10(ratio) #call out the 'log10' function from the math module to be used on ratio value.
			import math
			radians = 0.7
			height = math.sin(radians) #reference the 'sin' function from the math module to be used on the radians value.
			import math
			degrees = 45 #set initial value of degrees
			radians = degrees / 360.0 * 2 * math.pi #convert degree variable to radians by using math module 'pi function'.
			math.sin(radians) #now sine can be calculated on the inputted radians value
			math.sqrt(2)/2.0 #use square root function from math module to test equality to above.
		
	##Adding New Functions
		#A function definition specifies the name of a new function and the sequence of statements that execute when the function is called.
		#When a function is defined in a program, it can be reused over and over throughout that program.
		#A function is composed of a 'header' and 'body'...
			#...The 'header' uses command 'def' to define a function followed by the function name which ends in '()' and ':'...
			#...The 'body' must be indented in and will state what the function will output.
				def print_lyrics() : #define function 'print_lyrics() using the 'def' command.
					print ("I'm a lumberjack, and I'm okay.")
					print ("I sleep all night and I work all day.")
				print (print_lyrics) #states the function name
				print (type(print_lyrics)) #states the class of the function (function classes are functions)
				print_lyrics() #outputs the return value of the function
            #The 'definition' is when the function is created, but the 'call' or 'invoke' is when it is actually executed. 
            #Functions can be defined but never called.
            #Ending a function is completed by entering an empty line (not required in scripts).
			#Functions are their own types.
			#Functions can be called within one another, for example (referring to above, as well):
				def repeat_lyrics() : #define a function called 'repeat_lyrics()'
					print_lyrics() 
					print_lyrics() #repeats the previously defined function twice, when function 'repeat_lyrics()' is called
	
	##Definitions and Uses
		#When functions are defined, they are stored as 'function objects'.
		#Functions do not get evaluated until they are called by entering the function's name...
		#...The function definition generates no output.
		#Fundamentally, a function has to be created before it can be executed.
		
	##Flow of Execution
		#The order in which a function's statements are executed is the 'flow of execution'.
		#Execution occurs procedurally: statements are executed one at a time in order from top to bottom.
		#Function definitions do not alter the flow of execution, but statements are not executed until the function is called.
		#If a function call is a statement in a 'mother function' , all of the statements in that function are procedurally executed, after which the 'mother function' executes the next line after the sub-function call...
		#...Therefore, following the 'flow of execution' is safer than just superficially reading the programmed order of execution.
		
	##Parameters and Arguments
		#An argument states the rule of how a function's input is mapped to an output.
        #Parameters are the specific inputs in a function call that will be mapped to an output.
		#Functions can have multiple arguments.
			math.pow(<base> , <power>) takes the 'base' input and raises it to the 'power' input.
		#Functions are defined by inputting the general relationship between input and output by using a specific argument that can be generalized:
			def print_twice(bruce) :
				print(bruce)
				print(bruce) #calling this function will print bruce twice, but calling print_twice(<arbitrary input>) will output the <arbitrary input> twice...
			print_twice(arbitrary_input) #...moving from definition by specific argument (bruce) to being able to use the function for arbitrary input.
		#This principle of generalized function definition applies to other defined operator manipulations:
			#Assume definition of print_twice() is registered in the Python interpreter, then:
			print_twice('spam ' , *4) #prints 4 occurrences of 'spam' , two times.
		
	##Fruitful and Void Functions
		#Fruitful functions return a value, so it is an error to exclude the call to return in a fruitful function.
        #Set a variable equal to a fruitful function (includes return) with valid inputs, and that variable will contain the returned value/output of the fruitful function.
			import math
			print (math.sin(4)) #fruitful function because it maps 4 to the value equal to the sine of 4 radians
		#Void functions perform an action but do not return a value at the end (usefulness comes from printing statements while function executes).
		#Void functions include the 'print_twice' command as above, because the output is directly related to the fact that strings are printed.
		#In a Python script, calling a fruitful function will output that value, but it must be stored in a variable within the function if its value is to be referenced later.
		#Assigning a fruitful function output to a variable means that that variable will store the frutiful function's output.
			def addtwo(a,b) :
				added = a + b #add the two inputs of the addtwo() function
				return added #return statement sends the computed value to the calling code as the function result, set equal to the initial variable which the addtwo() function is assigned
				x = addtwo(3,5)
				print x #returns 8, or the value of addtwo() function
		#However, assigning a void function output to a variable will assign that variable the output 'none' ...
		#...the 'none' that is the equivalent of a void function is not the string 'none' , but is a special value of the type 'NoneType'.
		
	##Why are functions useful?
		#Creating functions names a group of statements in one place, which makes program easier to read, understand, and debug.
		#Functions can reduce a program's size by reducing repetitive code.
		#Once a function is tweaked, it can be reused in all relevant situations.
		
	##Debugging common sources of function errors
		#Use spaces exclusively (no tabs).
		#Save the program before running in the command prompt, changes will not be automatically updates.
		#Make sure the code you are looking at is the code you are running, easily testable by putting a print ('unique message here')...
		#...and checking that that message shows up.
		