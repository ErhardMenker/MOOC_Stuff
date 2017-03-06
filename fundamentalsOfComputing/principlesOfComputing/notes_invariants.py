### Invariants

# An invariant is a logical condition that repeatedly holds throughout the program.
# An invariant is guarenteed to evaluate to True at different points in the program.
# Invariants only need to be True when they are tested.

# Loop Invariants
def iterative_factorial(num):
    answer = 1
    index = 0
    assert answer == math.factorial(index)
    while index < num:
        index += 1
        answer *= index
        assert answer == math.factorial(index)
    return answer 