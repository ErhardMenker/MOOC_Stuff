%%% The Least Squares Normal Equation
% Least squares fit to data has an analytical solution (gradient descent is...
% ...numerical)
% Let X be an m by n + 1 matrix storing the m observations and the n features
% Note that the first column of X is a column of ones to represent intercept
% Let y be the m dimensional solution vector containing the outcome variable...
% ...for each of the observations
% In Octave, the normal equation to solve for the n dimensional vector of...
% ...each of the thetas is (starting with the intercept through the nth...
% ...attribute is: pinv(X' * X) * X' * y  
% Feature scaling is not necessary for when the normal equation is used
% Unlike gradient descent, the normal equation does not need a learning rate...
% ...selected and does not require multiple iterations but works slower when...
% ...there are many features since it is costly to invert an n by n matrix...
% ...for large n (features)
% Gradient descent is useful for linear regression with a large number of...
% ...features and when polynomial selection occurs
% In the normal equation, (X' * X) may not be invertible if there are...
% ...redundant features (perfect multicollinearity) or if m <= n (there are...
% ...more features n than there are observations m; delete some features or...
% ...regularize)
% (X' * X) should never be noninvertible in Octave because pinv is the...
% ...pseudoinverse



