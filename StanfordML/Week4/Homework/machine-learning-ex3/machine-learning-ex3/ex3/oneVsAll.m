function [all_theta] = oneVsAll(X, y, num_labels, lambda)
%ONEVSALL trains multiple logistic regression classifiers and returns all
%the classifiers in a matrix all_theta, where the i-th row of all_theta 
%corresponds to the classifier for label i
%   [all_theta] = ONEVSALL(X, y, num_labels, lambda) trains num_labels
%   logistic regression classifiers and returns each of these classifiers
%   in a matrix all_theta, where the i-th row of all_theta corresponds 
%   to the classifier for label i

% Some useful variables
m = size(X, 1);
n = size(X, 2);

% You need to return the following variables correctly 
all_theta = zeros(num_labels, n + 1);

% Add ones to the X data matrix
X = [ones(m, 1) X];

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the following code to train num_labels
%               logistic regression classifiers with regularization
%               parameter lambda. 
%
% Hint: theta(:) will return a column vector.
%
% Hint: You can use y == c to obtain a vector of 1's and 0's that tell you
%       whether the ground truth is true/false for this class.
%
% Note: For this assignment, we recommend using fmincg to optimize the cost
%       function. It is okay to use a for-loop (for c = 1:num_labels) to
%       loop over the different classes.
%
%       fmincg works similarly to fminunc, but is more efficient when we
%       are dealing with large number of parameters.
%
% Example Code for fmincg:
%
%     % Set Initial theta
%     initial_theta = zeros(n + 1, 1);
%     
%     % Set options for fminunc
%     options = optimset('GradObj', 'on', 'MaxIter', 50);
% 
%     % Run fmincg to obtain the optimal theta
%     % This function will return theta and the cost 
%     [theta] = ...
%         fmincg (@(t)(lrCostFunction(t, X, (y == c), lambda)), ...
%                 initial_theta, options);
%

% iterate through each outcome possibility
for label = 1:num_labels
    % make current iterated outcome the positive class, other outcomes negative
    y_iter = [y == label];
    % solve for the optimal theta
    [theta_iter, cost_prev] = deal(zeros(n + 1, 1), Inf);
    % continue gradient descent iff cost function decreases sufficiently
    while 1  
        [J, grad] = lrCostFunction(theta_iter, X, y_iter, lambda);
        % if the cost increased, gradient descent will blow up; start over
        if (J - cost_prev) > 0
            % set theta as random standard normals; init cost to infinity 
            [theta_iter, cost_prev] = deal(normrnd(0, 1, n + 1, 1), Inf);
        elseif (cost_prev - J) > 0.0000000000001
            cost_prev = J;
            theta_iter = theta_iter - 0.1 * grad;
        else
            break
        endif
    endwhile
    % tack on theta estimate for this class to respective row in alltheta
    all_theta(label, :) = theta_iter'; 
endfor










% =========================================================================


endfunction
