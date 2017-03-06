# Question 1
weighted_resids_squared <- function(x_points, weights, mu) {
    sum <- 0
    for(idx in 1:length(x_points)) {
         sum <- sum + weights[idx] * (x_points[idx] - mu) ^ 2
    }
    return(sum)
}

print(weighted_resids_squared(c(0.18, -1.54, 0.42, 0.95), c(2, 1, 3, 1), 0.1471))
print(weighted_resids_squared(c(0.18, -1.54, 0.42, 0.95), c(2, 1, 3, 1), 0.0025))
print(weighted_resids_squared(c(0.18, -1.54, 0.42, 0.95), c(2, 1, 3, 1), 0.3))
print(weighted_resids_squared(c(0.18, -1.54, 0.42, 0.95), c(2, 1, 3, 1), 1.077))

# Question 2
x <- c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
y <- c(1.39, 0.72, 1.55, 0.48, 1.19, -1.59, 1.23, -0.65, 1.49, 0.05)
DF <- data.frame(x, y)
coef(lm(y ~ 0 + x, DF)) # regress y on x but force the line through the origin 

# Question 3
data(mtcars)
coef(lm(mpg ~ wt, mtcars))

# Question 6
x <- c(8.58, 10.46, 9.01, 9.64, 8.86)
(x[1] - mean(x)) / sd(x)

# Question 7
x <- c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
y <- c(1.39, 0.72, 1.55, 0.48, 1.19, -1.59, 1.23, -0.65, 1.49, 0.05)
coef(lm(y ~ x))

# Question 9
x <- c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
mean(x)

