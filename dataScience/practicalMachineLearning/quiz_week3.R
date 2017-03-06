### Question 1
rm(list=ls())

# load the dataset
library(AppliedPredictiveModeling); data(segmentationOriginal); library(caret); library(rattle)
# subset the training and test set (based on the Case entry), eliminating the case entry
train <- segmentationOriginal[grep("Train", segmentationOriginal$Case), -2]
test <- segmentationOriginal[-grep("Train", segmentationOriginal$Case), -2]
# fit a CART estimation on the data using the rpart method/package
set.seed(125)
model <- caret::train(Class ~ ., data = train, method = "rpart")
head(predict(model, test)) # predict the first 6 observations from the test set (stored in factor)
# fit a dendrogram of the CART
rattle::fancyRpartPlot(model$finalModel) # we can infer from quiz options if DT can be solved

### Question 3
rm(list=ls())
# load the dataset
library(caret); library(pgmm); data(olive); olive <- olive[,-1] # drop the first column of the olive DF
# fit a CART estimation on the data via caret
model <- caret::train(Area ~ ., data = olive, method = "rpart")
predict(model, as.data.frame(t(colMeans(olive))))

### Question 4
rm(list=ls())
# load the dataset
library(caret); library(ElemStatLearn); data(SAheart); set.seed(8484)
# partition the data into training and test
train = sample(1:dim(SAheart)[1],size=dim(SAheart)[1]/2,replace=F)
trainSA = SAheart[train,]; testSA = SAheart[-train,]
set.seed(13234)
# function to determine accuracy levels
missClass <- function(values,prediction){sum(((prediction > 0.5)*1) != values)/length(values)}
# fit the glm
modelSA <- glm(chd ~ age + alcohol + obesity + tobacco + typea + ldl, family = "binomial",
             data = trainSA)
# calculate in-sample and out-of-sample error
predictInSmpl <- predict(modelSA, trainSA, type = "response"); paste("In Sample Error:", missClass(trainSA$chd, predictInSmpl))
predictOutSmpl <- predict(modelSA, testSA, type = "response"); paste("Out-of-Sample Error:", missClass(testSA$chd, predictOutSmpl))

### Question 5
rm(list=ls())
# load the dataset
library(dplyr); library(caret); library(ElemStatLearn); data(vowel.train); data(vowel.test)
# convert the y variable to a factor
vowel.test <- transform(vowel.test, y = as.factor(y)); vowel.train <- transform(vowel.train, y = as.factor(y))
# fit an RF and rank the importance of the variables
set.seed(33833)
dplyr::arrange(cbind(names(vowel.train)[-1], caret::varImp(randomForest(y ~ ., data = vowel.train))), desc(Overall)) 