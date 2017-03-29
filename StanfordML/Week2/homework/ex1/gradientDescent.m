function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
    % GRADIENTDESCENT Performs gradient descent to learn theta
    %   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
    %   taking num_iters gradient steps with learning rate alpha
     
    % Initialize some useful values
    m = length(y); % number of training examples
    J_history = zeros(num_iters, 1);

    for iter = 1:num_iters

        % ====================== YOUR CODE HERE ======================
        % Instructions: Perform a single gradient step on the parameter vector
        %               theta. 
        %
        % Hint: While debugging, it can be useful to print out the values
        %       of the cost function (computeCost) and gradient here.
        %

        % copy theta - we want to update terms simultaneously
        theta_copy = theta;
        
        % update the intercept
        theta_copy(1) = theta(1) - alpha * sum(X * theta - y) / m;
        % update each slope coefficient
        for idx = 2:length(theta)
            slope = sum((X * theta - y) .* X(:, idx)) / m;
            theta_copy(idx) = theta(idx) - alpha * slope;
        end
        
        % reassign these simul updated theta_copy values to theta
        theta = theta_copy;

        % ============================================================

        % Save the cost J in every iteration    
        cost = computeCost(X, y, theta)
        J_history(iter) = computeCost(X, y, theta);

    end

endfunction


