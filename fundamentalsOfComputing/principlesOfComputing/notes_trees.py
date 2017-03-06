### Trees

# A tree is a collection of nodes and edges (edges are paths connecting nodes, or different stages of the tree).
# The tree has a root node (which is no node's child) and a collection of subtrees, so it is defined recursivel.
# Unrooted trees are hierarchical, and so they do not overlap. There will be one less node than there are edges.
# Trees can be defined recursively; after the root node but before the base case where a tree has no children, nodes can be defined both by their parent trees and their subtrees.
# If a node has no subtrees then it is a leaf node. Else, it is an internal node.
# The height of a tree is the longest path between a root node and any existing leaf.

"""
Python definition of basic Tree class

IMPORTANT:  Some class methods assume that instances of the Tree class
always have a single parent (or no parent for the root). See problem #8
on homework #3 for more details.
"""


class Tree:
    """
    Recursive definition for trees plus various tree methods
    """
    
    def __init__(self, value, children):
        """
        Create a tree whose root has specific value (a string)
        Children is a list of references to the roots of the subtrees.  
        """
        
        self._value = value
        self._children = children
        
        
    def __str__(self):
        """
        Generate a string representation of the tree
        Use an pre-order traversal of the tree
        """
        
        ans = "["
        ans += str(self._value)
                   
        for child in self._children:
             ans += ", "
             ans += str(child)
        return ans + "]"

    def get_value(self):
        """
        Getter for node's value
        """
        return self._value

    def children(self):
        """
        Generator to return children
        """
        for child in self._children:
            yield child
                    
    def num_nodes(self):
        """
        Compute number of nodes in the tree
        """
        ans = 1
        for child in self._children:
            ans += child.num_nodes()
        return ans
    
    def num_leaves(self):
        """
        Count number of leaves in tree
        """
        if len(self._children) == 0:
            return 1
        
        ans = 0
        for child in self._children:
            ans += child.num_leaves()
        return ans

    def height(self):
        """
        Compute height of a tree rooted by self
        """
        height = 0
        for child in self._children:
            height = max(height, child.height() + 1)
        return height

    
def run_examples():
    """
    Create some trees and apply various methods to these trees
    """
    tree_a = Tree("a", [])
    tree_b = Tree("b", [])
    print "Tree consisting of single leaf node labelled 'a'", tree_a
    print "Tree consisting of single leaf node labelled 'b'", tree_b
    
    tree_cab = Tree("c", [tree_a, tree_b])
    print "Tree consisting of three node", tree_cab
    
    tree_dcabe = Tree("d", [tree_cab, Tree("e", [])])
    print "Tree consisting of five nodes", tree_dcabe
    print 
    
    my_tree = Tree("a", [Tree("b", [Tree("c", []), Tree("d", [])]), 
                         Tree("e", [Tree("f", [Tree("g", [])]), Tree("h", []), Tree("i", [])])])
    print "Tree with nine nodes", my_tree
    
    print "The tree has", my_tree.num_nodes(), "nodes,", 
    print my_tree.num_leaves(), "leaves and height",
    print my_tree.height()

    #import poc_draw_tree
    #poc_draw_tree.TreeDisplay(my_tree)
    
             
#run_examples()



"""
Python class definition for creation and 
evaluation of arithmetic expressions
"""

# import Tree class definition
import poc_tree

# Use dictionary of lambdas to abstract function definitions

OPERATORS = {"+" : (lambda x, y : x + y), 
            "-" : (lambda x, y : x - y),
            "*" : (lambda x, y : x * y),
            "/" : (lambda x, y : x / y),
            "//" : (lambda x, y : x // y),
            "%" : (lambda x, y : x % y)}


class ArithmeticExpression(poc_tree.Tree):
    """
    Basic operations on arithmetic expressions
    """
    
    def __init__(self, value, children, parent = None):
        """
        Create an arithmetic expression as a tree
        """
        poc_tree.Tree.__init__(self, value, children)
        
        
    def __str__(self):
        """
        Generate a string representation for an arithmetic expression
        """
        
        if len(self._children) == 0:
            return str(self._value)
        ans = "("
        ans += str(self._children[0])
        ans += str(self._value)
        ans += str(self._children[1])
        ans += ")"
        return ans
        
        
    def evaluate(self):
        """
        Evaluate the arithmetic expression
        """
        
        if len(self._children) == 0:
            if "." in self._value:
                return float(self._value)
            else:
                return int(self._value)
        else:
            function = OPERATORS[self._value]
            left_value = self._children[0].evaluate()
            right_value = self._children[1].evaluate()
            return function(left_value, right_value) 

def run_example():
    """
    Create and evaluate some examples of arithmetic expressions
    """

    one = ArithmeticExpression("1", [])
    two = ArithmeticExpression("2", [])
    three = ArithmeticExpression("3", [])
    print one
    print one.evaluate()
    
    one_plus_two = ArithmeticExpression("+", [one, two])
    print one_plus_two
    print one_plus_two.evaluate()
    
    one_plus_two_times_three = ArithmeticExpression("*", [one_plus_two, three])
    print one_plus_two_times_three
    
    import poc_draw_tree
    poc_draw_tree.TreeDisplay(one_plus_two_times_three)
    print one_plus_two_times_three.evaluate()
    
run_example()
        