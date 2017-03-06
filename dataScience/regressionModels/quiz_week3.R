### Question 1
data(mtcars)
summary(lm(mpg ~ factor(cyl) + wt, data=mtcars))$coef 
# Conclusion: 8 cylinders have an average mpg of 6.071 less than 4 cyls 

### Question 2
data(mtcars)
# model with weight confounder:
summary(lm(mpg ~ factor(cyl) + wt, data=mtcars))$coef 
# model without weight confounder:
summary(lm(mpg ~ factor(cyl), data=mtcars))$coef 
# Conclusion: the impact of the cylinder categorical variable is greater when weight is excluded

### Question 3
fit1 <- lm(mpg ~ factor(cyl) + wt, data=mtcars) 
fit2 <- lm(mpg ~ factor(cyl), data=mtcars) 
# Anova
anova(fit1, fit2, test="LRT")
# Conclusion: reject the null hypothesis of equivalent explanatory power of the 2 equations and...
# ...conclude that weight is a necessary confounding predictor variable

### Question 5 - 6
x <- c(0.586, 0.166, -0.042, -0.614, 11.72)
y <- c(0.549, -0.026, -0.127, -0.751, 1.344)
influence.measures(lm(y ~ x))
# Conclusion: the 5th point has the most leverage because it has the largest hat value and it...
# ...has a dfbeta of -134