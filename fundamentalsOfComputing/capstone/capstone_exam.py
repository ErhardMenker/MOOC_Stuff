'''
Fundamentals of Computing Capstone Exam
'''

'''
Question 1
'''
print
print "QUESTION 1:"

def null():
    return
    
q1 = null()
print q1

'''
Question 2
'''
print
print "QUESTION 2:"

var1 = 7

def var3(var1, var2):
    var0 = var1 + var2
    global var4
    var4 = 17
    return var0
    
print var3(3, 5)
print var4

'''
Question 3
'''
print
print "QUESTION 3:"

print {3: True, False: None}

'''
Question 5
'''
print
print "QUESTION 5:"

class BankAccount:
    def __init__(self, initial_balance):
        """
        Creates an account with the given balance.
        """
        self.balance = initial_balance
        self.fees = 0

    def deposit(self, amount):
        """
        Deposits the amount into the account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  
        Each withdrawal resulting in a balance of 
        less than 10 dollars (before any fees) also 
        deducts a penalty fee of 5 dollars from the balance.
        """
        self.balance -= amount
        if self.balance < 10:
            self.balance -= 5
            self.fees += 5

    def get_balance(self):
        """
        Returns the current balance in the account.
        """
        return self.balance

    def get_fees(self):
        """
        Returns the total fees ever deducted from the account.
        """
        return self.fees

account1 = BankAccount(10)
account1.withdraw(15)
account2 = BankAccount(15)
account2.deposit(10)
account1.deposit(20)
account2.withdraw(20)

print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()

account1 = BankAccount(20)
account1.deposit(10)
account2 = BankAccount(10)
account2.deposit(10)
account2.withdraw(50)
account1.withdraw(15)
account1.withdraw(10)
account2.deposit(30)
account2.withdraw(15)
account1.deposit(5)
account1.withdraw(10)
account2.withdraw(10)
account2.deposit(25)
account2.withdraw(15)
account1.deposit(10)
account1.withdraw(50)
account2.deposit(25)
account2.deposit(25)
account1.deposit(30)
account2.deposit(10)
account1.withdraw(15)
account2.withdraw(10)
account1.withdraw(10)
account2.deposit(15)
account2.deposit(10)
account2.withdraw(15)
account1.deposit(15)
account1.withdraw(20)
account2.withdraw(10)
account2.deposit(5)
account2.withdraw(10)
account1.deposit(10)
account1.deposit(20)
account2.withdraw(10)
account2.deposit(5)
account1.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account2.deposit(10)
account2.deposit(15)
account2.deposit(20)
account1.withdraw(15)
account2.deposit(10)
account1.deposit(25)
account1.deposit(15)
account1.deposit(10)
account1.withdraw(10)
account1.deposit(10)
account2.deposit(20)
account2.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account1.deposit(10)
account2.withdraw(20)

print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()

'''
Question 11
'''
print
print "QUESTION 13:"

print "The probability is: ", 1 / float(6 ** 4)

'''
Question 12
'''
print
print "QUESTION 12:"

def probability(rolls):
    '''
    calculate the probability of a dice outcome occurring, given a defined unfair dice
    '''
    # initialize the probability to 10
    prob = 1
    # mapping
    dice_probs = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.15, 5: 0.05, 6: 0.2}
    # iterate through the dice and adjust the probability of this chain
    for roll in rolls:
        prob *= dice_probs[roll]
        
    return prob

print "given probability: ", probability([4, 2, 6, 4, 2, 4, 5, 5, 5, 5, 1, 2, 6, 2, 6, 6, 4, 6, 2, 3, 5, 5, 2, 1, 5, 5, 3, 2, 1, 4, 4, 1, 6, 6, 4, 6, 2, 4, 3, 2, 5, 1, 3, 5, 4, 1, 2, 3, 6, 1])

'''
Question 17
'''
print
print "QUESTION 17:"

def pick_a_number(board, score1, score2, player):
    '''
    a recursive function that returns the optimal score for the switch-off game
    '''

    # player 1 to move
    if player == 1:
        # recursive case: more than 2 numbers are still on-the-board
        if len(board) >= 2:
            # if optimal, remove the first number
            if pick_a_number(board[1: ], score1 + board[-1], score2, 2)[0] >= pick_a_number(board[ :-1], score1 + board[0], score2, 2)[0]:
                first_number = board.pop(0)
                return pick_a_number(board, score1 + first_number, score2, 2)
            # if optimal, remove the last number
            else:
                last_number = board.pop()
                return pick_a_number(board, score1 + last_number, score2, 2)
        # base case: only one point is on the board (forced)
        else:
            return (score1 + board.pop(), score2)
                
    # player 2 to move
    if player == 2:
        # recursive case: more than 2 numbers are still on-the-board
        if len(board) >= 2:
            # if optimal, remove the first number
            if pick_a_number(board[1: ], score1, score2 + board[-1], 1)[1] >= pick_a_number(board[ :-1], score1, score2 + board[0], 1)[1]:
                first_number = board.pop(0)
                return pick_a_number(board, score1, score2 + first_number, 1)
            # if optimal, remove the last number
            else:
                last_number = board.pop()
                return pick_a_number(board, score1 + last_number, score2 + last_number, 1)
        # base case: only one point is on the board (forced)
        else:
            return (score1, score2 + board.pop())

print pick_a_number([3, 5, 2], 0, 0, 1)
            
'''
Question 25
'''
print
print "QUESTION 25:"

import itertools

def min_node_set(ugraph):
    '''
    algorithm to find the set of nodes such that every edge in the graph...
    has at least one point that belongs to the node set
    '''
    # place all of the nodes in a tuple
    nodes = list()
    for node in ugraph:
        nodes.append(node)
    nodes = tuple(nodes)
    
    # place all of the edge pairs in a list of tuples
    edges = list()
    for node, connects in ugraph.items():
        for connect in connects:
            edges.append((node, connect))
    
    for size in range(len(ugraph) + 1):
        # iterate through each combination of the outer loop's size
        for node_combo in map(set, itertools.combinations(nodes, size)):
            flag = True
            for edge in edges:
                # if an edge shares no node in common with the node_combo, then this isn't a feasible solution
                if node_combo.intersection(set(edge)) == set([]):
                    flag = False
                    break
            # return this node combination if it shares at least one node with every edge   
            if flag:
                return "node length:", len(node_combo), "node combo:", node_combo

print "capstone question:", min_node_set({1: set([2, 3, 4, 5, 6, 7]), 2: set([3]), 3: set([4]), 4: set([5]), 5: set([6]), 6: set([7])})                
print "graph 3:", min_node_set({0: set([4, 7, 10]), 1: set([5, 6]), 2: set([7, 11]), 3: set([10]), 4: set([0, 7, 11]), 5: set([1, 7]), 6: set([1]), 7: set([0, 2, 4, 5, 9, 11]), 8: set([9]), 9: set([7, 8]), 10: set([0, 3]), 11: set([2, 4, 7])})
print "graph 4:", min_node_set({0: set([4, 7, 10, 12, 13]), 1: set([5, 6, 12]), 2: set([7, 11, 12, 14]), 3: set([10, 14, 15]), 4: set([0, 7, 11, 12, 13, 14]), 5: set([1, 7, 15]), 6: set([1, 13]), 7: set([0, 2, 4, 5, 9, 11, 14]), 8: set([9, 14, 15]), 9: set([7, 8]), 10: set([0, 3]), 11: set([2, 4, 7]), 12: set([0, 1, 2, 4]), 13: set([0, 4, 6, 15]), 14: set([2, 3, 4, 7, 8]), 15: set([3, 5, 8, 13])})
print "graph 6:", min_node_set({0: set([4, 7, 10, 12, 13, 16]), 1: set([5, 6, 12]), 2: set([7, 11, 12, 14]), 3: set([10, 14, 15]), 4: set([0, 7, 11, 12, 13, 14, 17]), 5: set([1, 7, 15]), 6: set([1, 13]), 7: set([0, 2, 4, 5, 9, 11, 14, 18]), 8: set([9, 14, 15]), 9: set([7, 8, 19]), 10: set([0, 3]), 11: set([2, 4, 7]), 12: set([0, 1, 2, 4]), 13: set([0, 4, 6, 15, 16]), 14: set([2, 3, 4, 7, 8]), 15: set([3, 5, 8, 13]), 16: set([0, 13, 17, 19]), 17: set([4, 16]), 18: set([7]), 19: set([9, 16])})     
        
        
        
    

    
    