# variables - placeholders for important values
# used to avoid recomputing values and to
# give values names that help reader understand code


# valid variable names - consists of letters, numbers, underscore (_)
# starts with letter or underscore
# case sensitive (capitalization matters)

# legal names - ninja, Ninja, n_i_n_j_a
# illegal names - 1337, 1337ninja

# Python convention - multiple words joined by _
# legal names - elite_ninja, leet_ninja, ninja_1337
# illegal name 1337_ninja



# assign to variable name using single equal sign =
# (remember that double equals == is used to test equality)

# examples 

my_name = "Erhard Menker"
print my_name # returns: "Erhard Menker"

my_age = 22
print my_age #returns: 22

# birthday - add one

my_age += 1 #the += operator adds the LHS to the other values in the RHS, storing back in LHS variable
print my_age


# the story of the magic pill

magic_pill = 30
print my_age - magic_pill #outputs -8, or result of 22 - 30

my_grand_dad = 74

print my_grand_dad - 2 * magic_pill #returns 14, or value of 74 - 30*2

