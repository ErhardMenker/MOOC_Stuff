library(datasets)
data(iris)

# Question 1: Mean of Sepal.Length for virginica species
# Split the iris DF by the Species column, and for each element in this list, take mean of Sepal.Length
lapply(split(iris, iris$Species), function(elem) mean(elem[, "Sepal.Length"]))
# Take the Sepal.Length column, split by the Species vector, and take the mean of each species partition
tapply(iris$Sepal.Length, iris$Species, mean)

# Question 2: Code to Return a vector of means of the columns 1 to 4
apply(iris[, 1:4], 2, mean)

library(datasets)
data(mtcars)

# Question 3: Calculate the average miles per gallon by number of cylinders in the car
lapply(split(mtcars, mtcars$cyl), function(elem) mean(elem[, "mpg"]))
sapply(split(mtcars$mpg, mtcars$cyl), mean)
tapply(mtcars$mpg, mtcars$cyl, mean)
with(mtcars, tapply(mpg, cyl, mean))

# Question 4: Absolute difference between average horsepower of 4 and 8 cylinder cars
abs(tapply(mtcars$hp, mtcars$cyl, mean)[c("8")] - tapply(mtcars$hp, mtcars$cyl, mean)[c("4")])

# Question 5: Running the debugger
debug(ls)
ls