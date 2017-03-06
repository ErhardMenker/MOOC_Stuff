# dimensional problem of conditional execution

x <- 1:10
if(x > 5) {
    x <- 0
}

# lexical scoping

f <- function(x) {
    g <- function(y) {
        y + z
    }
    z <- 4
    x + g(x)
}

z <- 10
f(3) # z is set equal to 4 in g(y) because z is set to 4 at the same level of g's definition.

# conditional execution

x <- 5
y <- if(x < 3) {
    NA
} else {
    10
}

y 