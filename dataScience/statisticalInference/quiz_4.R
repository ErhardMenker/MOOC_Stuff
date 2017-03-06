### Question 1
baseline <- c(140, 138, 150, 148, 135)
week2 <- c(132, 135, 151, 146, 130)
t.test(baseline, week2, alternative="greater", paired=TRUE, var.equal=FALSE)$p.val

### Question 2
require(MASS)

data <- MASS::mvrnorm(9, mu=1100, Sigma=30**2, empirical=TRUE) 
t.test(data, alternative="two.sided", mu=1077)$p.value
t.test(data, alternative="two.sided", mu=1123)$p.value

### Question 3
p_val <- 0.5 ** 4 + 4 * 0.5 ** 4

### Question 4
ppois(10, 1787 * 0.01) # what's the prob I realized value as small as I did (10) if null is TRUE?

### Question 5
treatment <- MASS::mvrnorm(9, mu=-3, Sigma=1.5**2, empirical=TRUE)
placebo <- MASS::mvrnorm(9, mu=1, Sigma=1.8**2, empirical=TRUE)
t.test(treatment, placebo, alternative="two.sided")$p.val

### Question 7
# calculate the power of the test
power.t.test(n=100, delta=0.01, sd=0.04, type="one.sample", alternative="one.sided")$power

### Question 8
power.t.test(delta=0.01, sd=0.04, power=0.9, type="one.sample", alternative="one.sided")$n