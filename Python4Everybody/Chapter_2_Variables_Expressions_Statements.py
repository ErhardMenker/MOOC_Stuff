###Chapter 2: Variables, Expressions and Statements###
	
##Values and Types
	#A value is an input that a program works with. There are multiple types of values:
	#A string, classified as ‘str,’ is a collection of letters that are strung together.
		print('hello_world') ##this is a string
	#An integer, classified as ‘int,’ is a number that satisfies the mathematical definition of integer.
		11 ##this is an integer
	#A floating point, classified as ‘float,’ is a number that includes a decimal point.
		17.00 ##this is a float
	#Typing ‘type (<value>)’ returns the type of the inputted value. Strings must be inputted in quotes, but integers and floats will not be. 
		type(17.00) ##returns 'float'
	#Numbers inputted in quotes are classified as strings.
		type('17.23') ##returns 'string'
	#Commas cannot be inputted in integers or floats, because the program assumes these are comma separated integer sequence and will print out the numbers separately, but will error out for type classification.

##Variables
	#A variable is a name that refers to (or represents) a value and has examples with abundance:
	message = ‘I love econometrics’ ##sets the string ‘I love econometrics’ equal to the variable ‘message.’
	n = 17 ##sets the value 17 equal to the variable ‘n.’
	pi = 3.14152 ##sets the value 3.14152 equal to the variable ‘pi.’
	#An assignment statement is the act of creating new variables and setting them equal to their values.
	#For an arbitrary assigned variable, entering ‘print (<variable>)’ will output the value assigned to that variable, with strings stripped of their quotes. Note that the variable in the print statement shouldn’t be enclosed in quotes.
	#The type of a variable is the value that it has been assigned. So if ‘n = 17’ has been inputted, the type of n is integer.

##Variable Names and Keywords
	#Variable names can be arbitrarily long but they should reference what the variable can equal and/or will be used for.
	#A mnemonic (meaning ‘memory aid’) means that the variable is useful in that it closely resembles and carefully describes the value that it will be equal to. 
	#Variable names can include numbers and letters but cannot start with numbers or include illegal characters such as ‘@’. While upper case letters can be used, it is best to begin variables with lower case letters.
	#It is illegal for variables to be named one of Python’s reserved words such as ‘for.’
	#If one of Python’s variable naming conventions is violated, a syntax error is produced.
	#Variable names cannot include spaces because Python interprets these multiple values as operands without operators. In such cases, the underscore ‘_’ is often used for variables with multiple words.

##Statements
	#A statement is a unit of code that the Python interpreter can execute, such as printing or assigning. 
	#Output results from statements that print outputted values. These are the values outputted in the command prompt when a program is executed. A syntactically correct statement with no resulting prints is not classified as ‘output.’
	#A script will typically include multiple statements, which will be executed procedurally from the first line down.
	#If a script includes statements that prints an integer, assigns another integer equal to a variable and then prints that variable, the only resulting output are the two prints that occur. 

##Operators
	#An Operator is a special symbol that represents specific computations, such as addition, and includes:
	#‘+’ is an additive operator. 
		2+2 ##returns 4
	#‘-‘ is a subtractive operator.
		70-1 ##returns 69
	#‘*’ is a multiplicative operator.
		3*4 ##returns 12
	#‘**’ is an exponential operator raising the number below the ‘**’ to the number after.
		3**3 ##returns 27 
	#‘/’ is the floating division operator. The returned value is a float because the output is rounded to at least the tenth, even if the resulting value is mathematically an integer.
		6/4 ##returns 1.5
	#‘//’ is the integer division operator. Values are rounded down to the largest integer smaller than the resulting number, and typed as integers.
		6//4 ##returns 1
	#Parenthesis can be inputted to overwrite the defaulted orders of operations.
	#The modulus operator returns the remainder of an expression divided using the ‘%’ operator. An outputted value of ‘0’ means there is no remainder in the division. 
		8%3 ##returns 2, because the division of 8 by 3 equals 2 remainder 2)
	#The output of the modulus operator is an integer if the output is a mathematical integer, else it is a float.

##Expressions
	#An expression is a value, variable, operator, and any such combinations of these concepts.
		x = 17 ##set initial value of x
		x = x + 3 ##adds 3 to the initial value of x, storing that back in x
		print (x) ##outputs 20, the latest value of x
	#Python mathematical evaluation of expressions is subjected to the order of operations, such that an expression is evaluated in order by the components parenthesis, exponentials, multiplication/division, and addition/subtraction, with any of the same class of operations occurring in order from left to right.  

##String Operations
	#The ‘+’ operator is an additive operator for integers and floats.
		first = 10 ##set variable 'first' equal to integer 10
		second = 15 ##set variable 'second' equal to integer 15
		first + second ##returns 25, because the sum of integers
	#However, the '+' operator concatenates strings.
	#Concatenation is the act of joining multiple operands (typically strings) from end to end.
		first = '10' ##set variable 'first' equal to string '10'
		second = '15' ##set variable 'second' equal to string '15'
		first + second ##returns string '1015,' because strings have been joined end to end.
	#Inputting a comma between two string separates them.
		name = "Erhard" 
		age = "22"
		print (name , age)
	#Concatenation occurs in order of how the variables are listed when they are concatenated. 
	#Thus, unless all concatenated strings are equivalent, concatenation is not commutative.

##The Input Function
	#Setting an arbitrary string name equal to ‘input()’ empties a line in the interpreter in which a message can be inputted. Once the message is inputted, selecting enter returns the interpreter to normal and then printing the string returns the message:
	#Setting a string as a variable equal to the input function with a question ending with ‘\n’ as the input will return the question when executed, so the user can answer the question and will set the variable string equal to the inputted answer:
	#The ‘\n’ creates a new line, allowing the inputted response ‘Erhard’ in this case.
	#If a question prompts an integer response, the value can be recalled by using the int() command around the string’s name. This will work for neither floats nor integers.
		name =input("what is your name?"/n)
		Erhard
		print 'Hello' , name
	#The ‘input()’ command is ‘raw_input()’ in Python 2.
	

##Comments
	#Comments are messages left in a program that are ignored when the program is run.
	#Since it can ultimately be figured out what a code is trying to do, assuming proper syntax, good comments explain why the code is executing what it is.
	#Comments are used to clarify what is occurring in a program at a given time, since computing languages can be dense.
	#Comments are typically provided above what they are trying to explain, or immediately to the right.
