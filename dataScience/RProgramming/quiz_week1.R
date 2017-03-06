### Standalone Questions

# See what class x <- 4 is
x <- 4
class(x)

# Coercion test
x <- c(4, "a", TRUE)
x
class(x)

# Cbind two vectors
x <- c(1, 2, 3)
y <- c(4, 5, 6)
cbind(x, y)

# Subsetting question
x <- list(2, "a", "b", TRUE)
y <- x[[2]]
print(y)
class(y)
length(y)

# Adding vectors of different dimensions
x <- 1:4
y <- 2:3
x + y
class(x + y)

# Set all elements of a vector greater than 10 to equal 4
x <- c(17, 14, 4, 5, 13, 12, 10)
x[x > 10] <- 4
x

### DATA TIME!!!

# Move the R working directory to where the file will be written in; check this result.
setwd("C:/Data/Analytics_Studies/R/Data_Science_Specialization/R_Programming")
getwd()

# Read in the dataset and give it a handler called dframe
dframe <- read.csv(file="hw1_data.csv")
#print(dframe) # Show what the data frame looks like

# Column names?
names(dframe)

# Print out every column of the first two rows to console
dframe[1:2, ]

# How many observations (rows) exist in this data frame?
nrow(dframe)

# Extract the last two rows of this data frame
dframe[(nrow(dframe) - 1):nrow(dframe), ] # subset the second to last through the last row

# Ozone value in 47th row?
dframe[47, ]$Ozone

# How many Ozone values are missing?
sum(is.na(dframe$Ozone)) # subset the Ozone vector, get a logical vec of missing values, sum it

# Find non-NA average of Ozone values
mean(dframe$Ozone[!is.na(dframe["Ozone"])])

# Mean of Solar when Ozone exceeds 31 and Temp exceeds 90
mean(dframe$Solar[dframe$Ozone > 31 & dframe$Temp > 90][!is.na(dframe$Solar[dframe$Ozone > 31 & dframe$Temp > 90])])

# Mean of Temp when Month equals 6s
mean(dframe$Temp[dframe["Month"] == 6][!is.na(dframe$Temp[dframe["Month"] == 6])])

# Max Ozone value in Month equal to 5
max(dframe$Ozone[dframe["Month"] == 5][!is.na(dframe$Ozone[dframe["Month"] == 5])])