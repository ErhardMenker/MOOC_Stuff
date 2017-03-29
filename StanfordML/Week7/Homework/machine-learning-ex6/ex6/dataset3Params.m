function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;
% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

% Set the landmarks to the observed y output 
x1 = y; x2 = y;

% Initialize the lowest CV misclassification error to the highest possible
cvErrorLow = 1; 

COptions = [.01, .03, .1, .3, 1, 3, 10, 13];
sigmaOptions = [.01, .03, .1, .3, 1, 3, 10, 13];

% Iterate through & calculate the CV error based on reg param (C) & sigma ^ 2
for C = COptions
    for sigma = sigmaOptions 
        % 1) train the SVM with reg param C
        % 2) predict using this SVM on the CV set 
        % 3) calculate the misclassification error on the CV 
        cvError = mean(double(svmPredict(svmTrain(X, y, C, @(x1, x2) ... 
                        gaussianKernel(x1, x2, sigma)), Xval) ~= yval));
   
        % if the CV error is the lowest so far, give it this status
        if cvError <= cvErrorLow 
            cvErrorLow = cvError; 
            minC = C;
            minSigma = sigma; 
        endif 
    endfor
endfor 

C = minC;
sigma = minSigma;



% =========================================================================

end
