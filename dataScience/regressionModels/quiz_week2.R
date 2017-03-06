## Question 1 & 2
x <- c(0.61, 0.93, 0.83, 0.35, 0.54, 0.16, 0.91, 0.62, 0.62)
y <- c(0.67, 0.84, 0.6, 0.18, 0.85, 0.47, 1.1, 0.65, 0.36)
# regress y against x
summary(lm(y ~ x))
summary(lm(y ~ x))$sigma

## Question 3
data(mtcars)
# regress weight on mpg
fit_q3 <- lm(mpg ~ wt, data=mtcars)
predict(fit_q3, newdata=data.frame(wt=mean(mtcars$wt))) + 
    c(-1, 1) * qt(0.975, df=summary(fit_q3)$fstatistic[3]) * summary(fit_q3)$coefficients[2, 2] 

## Question 5
require(plyr)
data(mtcars)
mtcars <- plyr::mutate(mtcars, wt = 1000 * wt)
# regress weight on mpg
fit_q5 <- lm(mpg ~ wt, data=mtcars)
predict(fit_q5, newdata=data.frame(wt=3000)) + 
    c(-1, 1) * qt(0.975, df=summary(fit_q5)$fstatistic[3]) * summary(fit_q5)$coefficients[2, 2]

## Question 6
require(plyr)
data(mtcars)
mtcars <- plyr::mutate(mtcars, wt = 0.5 * wt)
# regress weight on mpg
fit_q6 <- lm(mpg ~ wt, data=mtcars)
summary(fit_q6)$coefficients[2, 1] + 
    c(-1, 1) * summary(fit_q6)$coefficients[2, 2] * qt(0.975, df=summary(fit_q6)$fstatistic[3])

## Question 9
data(mtcars)
fit_slope <- lm(mpg ~ wt, data=mtcars)
fit_noslope <- lm(mpg ~ 1, data=mtcars)
# ratio:
sum(resid(fit_noslope) ^ 2) / sum(resid(fit_slope) ^ 2)