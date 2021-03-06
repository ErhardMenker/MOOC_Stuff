%%% Multivariate Linear Regression
% Often times it is better to use more predictors to predict an outcome...
% ...variable because the outcome variable is a function of many features
%% Multivariate Linear Regression Notation
% m is the number of observations
% n is the number of predictors
% x(i) is the ith observation in the training set
% x_sub_j(i) is the jth predictor value for the ith observation in training set
% The hypothesis function for the predictor vector y is...
% beta(0) + beta(1) * x1_sub_j + ... + beta(n) * xn_sub_j
% This predictor vector says that each of its entries is equal to the...
% ...intercept plus the sum product of each of its values multiplied by their...
% ...respective coefficients
% For convenience of notation, the intercept vector in the summation is often...
% ...expressed as the ones vector scalar multiplied by the intercept's...
% ...coefficient value (analogous to the slope term in any other term)

%% Gradient Descent for Multivariate Regression Introduction
% Each parameter is updated (simultaneously) in similar fashion to univariate...
% ...linear regression and there are as many parameters as there are features...
% ...plus one (remember the intercept), or n + 1

%% How to make gradient descent converge faster
% 1) Feature Scaling - if variables are on a different range, the plot of the...
% ...data becomes very skewed and the algorithm can take a long & convoluted...
% ...path to reaching the minima. Putting the values on a similar scale by...
% ...scalar multiplication accelerates convergence by reducing skew 
% A good rule of thumb is to scale every variable such that it ranges from...
% approximately -1 to 1
% Mean normalization can be executed on a vector by subtracting the vector's...
% ...mean and dividing that value by the vector's range or standard deviation
% 2) Selecting the learning rate - recall that if alpha is too small, the...
% ...learning algorithm is prohibitively slow, but if alpha is too large, the...
% ...algorithm could fail to converge 
% One rule could be to declare convergence if the cost function gets lowered...
% ...by less than a certain threshold after another iteration, but choosing...
% ...this threshold can be difficult (depends on the context of the problem)
% Another possibility is to look at plots that graph the cost function as a...
% ...function of the amount of iterations gradient descent has taken for...
% ...different learning rates to determine the optimal learning rate 
% If the cost function is increasing as a function of iterations, that is an...
% ...indication that the learning rate alpha is too large 
% For sufficiently small alpha, the cost function should decrease on every...
% ...iteration 

%% Features and Polynamial Regression
% Sometimes linearity does not best capture the relationship between a...
% ...predictor and the outcome variable
% Example: as housing size continues to rise, the increase in price can begin...
% ...to vanish so it may be advantageous to include a square root term
% These terms can be captured by doing the transformation on the data...
% ...directly and then doing least squares estimation
% Feature scaling becomes very important under polynomial transformations...
% ...because some of the values can explode, making convergence difficult
% Algorithms exist to test optimal polynomial term selection



















