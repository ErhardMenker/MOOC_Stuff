### Question 1-3

# download the shuttle dataset from the MASS package
require(MASS)
data(shuttle)
# label "auto" as 1 and "noauto" as 0 in the "use" column; label "head" as 1 and "tail" as 0...
# ...in the "wind" column
shuttle <- transform(shuttle, use=sapply(shuttle$use, function(x) if(x == "auto") {1L} else {0L}),
                     wind=sapply(shuttle$wind, function(x) if(x == "head") {1L} else {0L}))

# fit a logit of whether the use is auto as a function of whether the wind is head
exp(summary(glm(use ~ wind, family="binomial", data=shuttle))$coef)
# fit a logit of whether the use is auto as a function of whether the wind is head
exp(summary(glm(use ~ wind + factor(magn), family="binomial", data=shuttle))$coef)
# see how the elasticity changes when you invert the binary outcome
summary(glm(use ~ wind + factor(magn), family="binomial", data=shuttle))$coef
summary(glm(I(1 - use) ~ wind + factor(magn), family="binomial", data=shuttle))$coef

### Question 4
data(InsectSprays)
# estimate count as a function of the spray factor using a poisson assumption (because count data)
summary(glm(count ~ relevel(factor(spray), "B"), family="poisson", data=InsectSprays))