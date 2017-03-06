### Question 1
rm(list=ls())
# load the Alzheimer disease data
library(AppliedPredictiveModeling); library(caret)
data(AlzheimerDisease)
adData <- data.frame(diagnosis, predictors)
trainIndex <- createDataPartition(diagnosis, p = 0.50,list=FALSE) # index matrix of training rows
training <- adData[trainIndex, ] # split out the rows corresponding to training data
testing <- adData[-trainIndex, ] # split out the rows corresponding to not training data (test data)

### Question 2-3
rm(list=ls())
# load the concrete data
library(AppliedPredictiveModeling); library(Hmisc); library(caret)
data(concrete)
set.seed(1000)
# place 75% of the observations into the training set
inTrain <- createDataPartition(mixtures$CompressiveStrength, p = 3/4)[[1]]
training <- mixtures[inTrain, ]
testing <- mixtures[-inTrain, ]
# create a histogram of the Superplasticizer column
hist(mixtures$Superplasticizer)
# find the minimum of the Superplasticizer column
min(mixtures$Superplasticizer)
head(log(mixtures$Superplasticizer)) # look at those negative infinite values!

# Question 4
rm(list=ls())
# load the alzheimer data
library(caret); library(AppliedPredictiveModeling)
set.seed(3433)
data(AlzheimerDisease)
adData <- data.frame(diagnosis,predictors)
inTrain <- createDataPartition(adData$diagnosis, p = 3/4)[[1]]
training <- adData[inTrain, ]; testing <- adData[-inTrain, ]
DF_PCA <- training[ , grep("^IL_", names(training))] # do PCA on columns titled beginning with "IL"
caret::preProcess(DF_PCA, method="pca", thresh=0.9) # return enough columns to reduce 90% of variance

# Question 5
rm(list=ls())
# load the alzheimer data
library(caret); library(magrittr); library(plyr); library(AppliedPredictiveModeling)
set.seed(3433)
data(AlzheimerDisease)
adData <- data.frame(diagnosis, predictors)
inTrain <- createDataPartition(adData$diagnosis, p = 3/4)[[1]]
training <- adData[inTrain, ]; testing <- adData[-inTrain, ]
DF_ESTM <- cbind(diagnosis = training$diagnosis, training[ , grep("^IL_", names(training))])
# logistic regression on the training data frame
eq_norm <- glm(diagnosis ~ ., data = DF_ESTM, family=binomial)
# test the equation fit on the testing data
testing$model_prob <- predict(eq_norm, testing, type = "response")
# code the prediction and actual values for the diagnosis as Booleans
testing <- testing %>% plyr::mutate(model_pred = 1 * (model_prob > 0.5) + 0,
                                    diagnosis_binary = 1 * (diagnosis == "Control") + 0)
# create a column "accurate" which is 1 if the prediction and actual are equivalent
testing <- testing %>% plyr::mutate(accurate = 1 * (model_pred == diagnosis_binary))
# see what proportion of the rows are "accurate"
paste("The proportion of accurate predictions for the regular model is:",  
      as.character(sum(testing$accurate)/nrow(testing)))






