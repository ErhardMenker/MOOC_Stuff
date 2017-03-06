###Algorithmic Efficiency

#Many syntactically correct algorithms can be developed for a problem but they may not be equally in terms of efficiency.
#Sometimes there is a tradeoff between efficiency and implementability.
#The fundamental judgments of algorithmic efficiency are time (how long does it take to run?) and space (how much memory does it take?)
#Time efficiency judges how many executions the algorithm will be expected to complete, not how much time is needed (requires knowledge of the computer power/programming language).
#There is often a tradeoff between time and space efficiency in analyzing different solutions, this course focuses on time efficiency.
#Algorithmic efficiency is judged based on the problem and general solution and not the underlying programming language.
#Judging algorithmic efficiency requires a great understanding of the problem and the relevant data structures that will be used.
#The time it takes for an algorithm to execute is typically a function of the input's size, as that will dictate what the number of raw executions are needed to solve the algorithm.

#Example: the size of a list is the number of elements in it, so the algorithm's run time on a list is a function of how many elements are in the list.
#Example: the size of a graph is usually judged as the number of nodes and/or edges, and the run time is a function of these nodes and/or edges.

#An assumption of judging algorithmic efficiency is that every individual base operation (multiplication, division, calling a function, returning a value, etc) is equal in time.
#Algorithms can be judged by worst/best/average case analysis, which asks what input into an algorithm will cause the algorithm's running time to be longest/average/shortest, respectively