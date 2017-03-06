###Chapter 3: Conditional Code###

##Boolean Expressions
	#A boolean expression is an expression that is either True or False.
		5 == 5 ##Returns 'True'
		5 == 6 ##Returns 'False'
	#'True' and "False" are not strings, but belong to the 'bool' type.	
	#The first and only first letter of these logical operators are capitalized.
	#Comparison operators test equality between multiple expressions, and include:
		x = 3
		y = 4 ##Initialize x and y values for comparison
		x != y #Returns 'true' if x does not equal y, 'false' otherwise
		x > y #Returns 'true' if x is greater than y, 'false' otherwise
		x < y #Returns 'true' if x is less than y, 'false' otherwise
		x >= y #Returns 'true if x greater than or equal to y, 'false' otherwise
		x is y #Returns 'true' if x is the same as y, 'false' otherwise ('is' and 'is not' best to used for testing special types like Booleans and None)
		x is not y #Returns 'true' if x is not the same as y, 'false' otherwise
	#x = y is improper Boolean notation because this sets x equal to y, since '=' is the assignment operator.
	# =< and => is improper notation
	
##Logical Operators
	#The three logical operators are 'and' 'or' 'not' , with semantics similar to their English meanings.
		#'And' condition returns true iff all condtions are true:
			x > 0 and x < 10 #true iff x is greater than 0 AND less than 10
		#'Or' condition returns true iff at least one of the conditions are true:
			y%2 == 0 or y%3 == 0 #true iff y is divisible by 2 OR y is divisible by 3
		#'Not' negates a boolean; returns true iff the negated argument is false and vice versa:
			not(x > y) returns true only if x is less than or equal to y
	#Python is not very strict Booleanwise; any nonzero number is interpreted as "true."
		17 and True ##returns 'true' because '17' is classified as 'True,' so both conditions hold 
		
##Conditional Execution
	#Conditional statements check conditions and change the program's behavior based on results.
		if x > 0 : #Boolean expression after the 'if statement' is the condition, to be followed by a ':'
			print ('x is positive') #If the above condition holds, the indented statement is executed. Else, it is skipped.
	#'If statements' are compound statements because they stretch across more than "one line.
	#The 'if statement' consists of a header line stating a condition that ends with the colon character, followed by an indented block of code called the 'body' (same structure as 'for loops' and 'functions').
	#The amount of statements that can appear in the 'body' must be at least one, with no upper bound.
	#"One way decisions" means that a procedure is executed if a condition holds.
    #It is possible to input the 'pass statement' to have a syntactically proper conditional execution with no statements.
		if x < 0 :
			pass #Need to handle negative values (code to be written in later)
	#Entering an 'if statement' in the Python interpreter will change from 3 chevrons (arrows) to 3 dots to indicate you are in block statements.
	#Python is sensitive to indents, and the body of code that is part of the loop or condition must be indented in 4 spaces beyond the colon.
    #Python sees spaces and tabs differently and errors with this inconsistency are "indentation errors". Turn off tabs in notepad ++ by going to settings -> preferences -> tab settings
    #The end of indented code in the body means that that "block" of code is over, serving the same purpose as the 'endif command' in EViews for 'if statements'.
    
##Alternative Execution
	#'Alternative execution' occurs when an 'if statement' has two possibilities ("two way decision), with the condition determining which one gets executed depending on if the condition holds...
    #...At most one condition will hold true in an 'if block', because once one condition holds true, the program exits the 'if block'.
        if x < 2 :
            print('below 2')
        if x < 20 :
            print('below 20')
        if x < 10 :
            print('below 10') #This line will never execute; if x is less than 10 it is less than 20 so that line would have executed and the if statement would exit then.
        
        if x%2 == 0 : #condition checks whether x is divisible by 2
			print ('x is even') #message to be printed if condition holds
		else :
			print ('x is odd') #message to be printed if condition does not hold
	#The alternatives that can be printed are called 'branches' , because they are different steps the code will take based on the condition holding or not.
	
##Chained Conditionals
	#More than two outcomes possible in an 'if statement' means more than two branches are possible.
	#The 'elif condition' is used, where 'elif' is a portmanteau of 'else if'.
	#'elif' allows the statement of another condition to follow, just as in the initial 'if condition', to be followed by a ':'.
		if x < y :
			print ('x is less than y') #message to be printed if x is less than y
		elif x > y :
			print ('x is greater than y') #message to be printed if x exceeds y
		else :
			print('x and y are equal') #message to be printed if x and y maintain equality
	#The limit on 'elif statement' numbers does not exist.
	#There does not need to be an 'else clause', but if there is, it must be at the end of the 'if statement' body.
	#Each statement is checked in order (procedurally)...
	#...The first time a condition holds, that condition's command is executed and the statement ends, even if later conditions are also true.
	
##Nested Conditionals
	#If statements can be nested with another:
		if x == y :  #the outer condition contains only two branches...
			print ('x and y maintain equality')
		else :
			if x < y : #...but the second condition nests another two branch 'if statement' within!!!
				print('x is less than y')
			else :
				print('x is greater than y')
	#Nested conditionals become difficult to read very quickly, avoid them if possible by using 'elif.'
	#Logical operators can simplify nested conditoinal statements by joining otherwise separate conditions:
		if 0 < x :
			if x < 10 :
				print ('x is greater than 0 but less than 10')
		#above code is semantically equivalent to this structured code with one less line:
		if 0 < x and x < 10 :
			print ('x is greater than 0 but less than 10')
			
##Catching Exceptions with 'Try and Except'
	#'Try and except' is a useful concept for debugging.
	#The procedure involves trying to execute the entirety of a 'try' sequence of code.
	#If any of the 'try' code body cannot be executed, the computer executes the 'except' code (often an informative error message).
	#The process of stopping logical execution once the logical outcome is guarenteed is called 'short-circuiting'.
	#Handling an exception with a 'try statement' is called 'catching an exception', by giving the opportunity to debug a 'semantic error'.
        astr = "Hello Bob"
        try : #try to execute the following code. If no error occurs in execution, exit 'try and except.'
            istr = int(astr) 
        except : #if there is an error in the 'try' body, execute the indented code in the 'except' body.
            istr = -1
    #If one or more lines of code is executed before an error in the 'try block', that execution will remain but any further lines will not be executed...
    #...but the 'except block' will still be executed.
    #It is good to put minimal code in the 'try block' so it is clear where the error occurs if the 'except block' is executed.
    
##Short-circuit Evaluation of Logical Expressions
	#Python processes multiple logical conditions by evaluating the conditions from left to right.
	#When Python detects that nothing is to be gained by evaluating more logical conditions, it stops execution.
		x = 1
		y = 0
		x >= 2 and (x/y) > 2 
			#Evaluates to false by definition of 'and' logical operator: because x is not >= 2 and is first condition, enough code is executed to know both conditions don't hold...
			#...Code was syntactically executed even though the second condition would result in an error if evaluated, because of the 'short-circuit' rule.
		x = 6
		y = 0
		x >= 2 and (x/y) > 2
			#Syntax error results from division by zero, since second condition must be executed because first code is true given 'and' logic.
	#A 'guard condition' can be imposed to prevent execution of code that could result in a syntax error:
		x = 6
		y = 0
		x >= 2 and y != 0 and (x/y) > 2 #Syntax error prevented, because third logical condition will only be executed if 'guard condition' of y not equaling 0 holds.
		
##Debugging
	#The traceback Python displays when an error occurs. 
	#The most useful information in the traceback message is usually:
		#What kind of error occurred (syntax or logical)?
		#Where it occurred?
	#Even so, often times Python will not think that code has been broken until after the error occurs.
	#Generally, debugging can be done by printing intermediate values that might not be needed to be printed in the 'production ready' script...
	#...Printing these intermediate values can show if there is cause for later syntax error, such as dividing by zero or logging a negative number.
	#Placing 'guards' and using 'try and except' can also show when code has been broken.
	#Improper indents are often a cause for syntax error.
		
	
		
	
		
			
		