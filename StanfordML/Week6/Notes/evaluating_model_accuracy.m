%%% Advice for Applying Machine Learning

%% Motivation
% It is necessary to give context to understand how to tackle an ML program...
% ...by evaluating different avenues and having wisdom to discern which way...
% ...is best, transcending knowledge of any 1 algorithm

%% Thinking about a model's accuracy/fruitfulness
% Suppose you use regularized linear regression to predict housing prices,...
% ...but there is large error, what should you do?
% To increase accuracy, you could change lambda, add/remove features, or add...
% ...polynomial terms, or increase training size (does not work if underlying...
% ...model is flawed)
% Often times people use gut feel to make these decisions; this is an...
% ...arbitrary decision that can result in unimproved accuracy after...
% ...implementation
% Use a diagnostic (a test that gives insight to see what is (not) working...
% ...for an ML algorithm)
% Diagnostics are often time heavy to implement but worth it because of the...
% ...insight they give 

%% Evaluating a Hypothesis
% If a hypothesis is overfitted, it fails to generalize to the test set 
% 1) Split initial dataset randomly into a training set (70%) & test set (30%)
% 2) Learn theta parameters from the training set 
% 3) Apply the theta parameters to the test set & calculate the test error
% For classification problems, execute the same steps but calculate the...
% ...misclassification error (% of judgements that are false positive/negative)

%% Model Selection & Training/Test/Validation Sets
% The training set error is not a good test of accuracy because error is...
% ...lowered in the scenario as more & more features are added
% Never use the test set to help fit a model by providing an error judgment...
% ...criterion; split the original data into training (60%),...
% ...cross validation (20%), and test (20%) where the validation set is used...
% ...to iteratively test an out-of-sample error and the test set is used...
% ...to report measures of accuracy only when the model is no longer...
% ...undergoing training 
% The model is implicitly fitting to the cross validation set since the...
% ..."out-of-sample" error measure is being used to make fitting judgments...
% ...therefore, the test set gives the best representation of the "final"...
% ...model error because its structure has no impact on the fitting process 

%% Diagnosing Bias vs Variance 
% The problem in an ML algorithm usually stems from high bias (underfit) or...
% ...high variance (overfit)
% As more features are added, the in-sample training error will decrease but...
% ...the out-of-sample test/validation error will decrease then increase when...
% ...overfitting kicks in 
% If there is high bias (underfitting), the training & test set errors will...
% ...both be high & not very unequal
% If there is high variance (overfitting), the training set errors will be...
% ...low while the test set errors are high (very unequal error magnitudes)

%% Regularization and Bias/Variance
% For a fixed model spec, a larger value of lambda shrinks the theta...
% ...magnitudes towards 0, reducing overfitting 
% For a model spec, the optimal lambda value is the 1 that minimizes the...
% ...CV error for the thetas trained with that lambda 
% The cost function is minimized with lambda but the training & CV cost...
% ...functions do not have lambda when comparing the fits for selection  
% A too small lambda will result in a high out-of-sample error because of...
% ...overfitting while a too large lambda will result in high out-of-sample...
% ...error as the shrinkage of coefficients towards 0 causes underfitting 

%% Learning Curves
% A learning curve is the process of calculating average error as a function...
% ...of incrementally increased observations (increasing m)
% The average training error typically increases with m, because it is easy...
% ...to fit a curve with a polynomial when there are less outcomes to predict
% If a model suffers from high bias, adding more training obs will not...
% ...sufficiently decrease the CV error because the model is missing a...
% ...fundamentally underlying pattern in the data
% If a learning algorithm suffers from high bias, adding more data does not...
% ...help substantially because the model spec just misses the underlying...
% ...polynomial pattern, so adding new data won't allow for these...
% ...polynomial terms to be trained since they're not in the model spec
% If a model suffers from high variance, there is a substantial gap in the...
% ...training & CV learning curves because the training model is not easily...
% ...extrapolated towards new data not trained upon
% In the case of high variance, adding more training data is helpful because...
% ...for all the polynomial terms, the true underlying pattern can become fit...
% ...better & extrapolated towards new data (in the limit they should converge)

%% Revisiting Debugging a Learning Algorithm
% Adding more training examples is more useful if the learning algorithm...
% ...suffers from high variance 
% Adding more features helps high bias algorithms; removing features helps...
% ...high variance algorithms 
% Adding more polynomial terms is more helpful for high bias fits 
% Decreasing lambda fixes high bias; increasing lambda fixes high variance 
% Using larger neural networks with regularization are typically more...
% ...accurate than smaller neural networks, but more computationally expensive






 







