setwd("C:/Data/Analytics_Studies/R/Data_Science_Specialization/Practical_Machine_Learning")

### Question 1
## data & workspace prep
rm(list=ls())
library(caret); library(ElemStatLearn); data(vowel.train); data(vowel.test)
test <- transform(vowel.test, y = as.factor(y)); train <- transform(vowel.train, y = as.factor(y))

## Random Forest Estimate & Predict
set.seed(33833); modFitRF <- caret::train(y ~ ., data = train, method = "rf")
predRF <- predict(modFitRF, test); paste("RF accuracy:", sum(predRF == test$y) / length(predRF))

## Boosting Estimate & Predict
set.seed(33833); modFitGBM <- caret::train(y ~ ., data=train, method = "gbm", verbose = FALSE)
predGBM <- predict(modFitGBM, test); paste("GBM accuracy:", sum(predGBM == test$y) / length(predGBM))

## If RF & GBM agree, what is the accuracy?
paste("agreement accuracy:", sum(predRF == predGBM & predGBM == test$y) / sum(predRF == predGBM)) 

### Question 2
## data & workspace prep
rm(list=ls())
set.seed(3433)
library(caret); library(gbm); library(AppliedPredictiveModeling); data(AlzheimerDisease)
adData <- data.frame(diagnosis, predictors)
# split the data into training & test sets
inTrain <- createDataPartition(adData$diagnosis, p = 3/4)[[1]]
training <- adData[inTrain, ]; testing <- adData[-inTrain, ] 

## predict using RF, GBM, LDA, and the Ensembler
set.seed(62433)
## RF
modFitRF <- caret::train(diagnosis ~ ., data = training, method = "rf")
predRF <- predict(modFitRF, testing)
paste("RF accuracy:", sum(predRF == testing$diagnosis) / length(testing$diagnosis))

## GBM
modFitGBM <- caret::train(diagnosis ~ ., data = training, method = "gbm", verbose = FALSE)
predGBM <- predict(modFitGBM, testing)
paste("GBM accuracy:", sum(predGBM == testing$diagnosis) / length(testing$diagnosis))

## LDA
modFitLDA <- caret::train(diagnosis ~ ., data = training, method = "lda", verbose = FALSE)
predLDA <- predict(modFitLDA, testing)
paste("LDA accuracy:", sum(predLDA == testing$diagnosis) / length(testing$diagnosis))

## Ensembler
# merge the 3 predictor factors of the test set into a DF with the actual diagnosis test set values 
predDF <- data.frame(predRF, predGBM, predLDA, diagnosis = testing$diagnosis)
# in new DF created for ensembler, predict the diagnosis using the 3 other predictors
modFitENS <-  caret::train(diagnosis ~ ., method = "rf", data = predDF)
predENS <- predict(modFitENS, testing)
paste("Ensembler accuracy:", sum(predENS == testing$diagnosis) / length(testing$diagnosis))

### Question 3
## data & workspace prep
rm(list=ls())
library(glmnet); library(AppliedPredictiveModeling); data(concrete)
set.seed(3523); inTrain = createDataPartition(concrete$CompressiveStrength, p = 3/4)[[1]]
training = concrete[inTrain, ]; testing = concrete[-inTrain, ]

## fit lasso while iteratively increasing lambda
lambdaHat = 0
repeat {
    set.seed(233)
    modFitLasso <- glmnet::glmnet(y = training[ , c("CompressiveStrength")], 
                        x = as.matrix(training[ , -which(names(training) == "CompressiveStrength")]),
                        lambda = lambdaHat)
    # if there is only one variable greater than 0, return the coefficient list and break from repeat 
    if (sum(sapply(modFitLasso$beta[ , 1], function(x) if(abs(x) > 0L) {TRUE} else {FALSE} == 1)) == 1) {
        print(paste("lowest lambda resulting in only 1 non-zero coefficient", lambdaHat)) 
        print("Lasso coefficients for this lambda value:")
        print(modFitLasso$beta[ , 1])
        break
    # if there are more than one variables greater than 0, add to lambdaHat and reiterate
    } else { 
        lambdaHat <- lambdaHat + 0.1
    } 
}

### Question 4
rm(list=ls())
## data & workspace prep
library(lubridate); library(forecast) 
dat = read.csv("./data_files/gaData.csv")
training = dat[lubridate::year(dat$date) < 2012,]; testing = dat[(lubridate::year(dat$date)) > 2011,]
# convert the visitsTumblr column of the training DF to the time series class
tstrain = ts(training$visitsTumblr)

## forecast & predict
predBATS <- predict(forecast::bats(tstrain), ts(testing$visitsTumblr))

### Question 5
rm(list=ls())
## data & workspace prep
set.seed(3523)
library(hydroGOF); library(caret); library(e1071); library(AppliedPredictiveModeling); data(concrete)
inTrain = caret::createDataPartition(concrete$CompressiveStrength, p = 3/4)[[1]]
training = concrete[ inTrain,]; testing = concrete[-inTrain,]

set.seed(325)
## fit & predict an SVM
modFitSVM <- e1071::svm(CompressiveStrength ~ ., data = training)
predSVM <- predict(modFitSVM, testing)
# calculate the RMSE
RMSE <- hydroGOF::rmse(predSVM, testing$CompressiveStrength)
paste("The RMSE of the test set is:", RMSE)


