% Octave is a free & open source high level language conducive to machine...
% ...learning

% In Octave, prefacing a line of code with "%" indicates a comment

% Basic Arithmetic Operations
1 + 1 % 2
3 - 1 % 2
5 * 8 % 40
1 / 2 % 0.5 (floating point division)
2 ^ 6 % 64

% Logical Tests 
1 == 2 % false (testing equality)
1 ~= 2 % true (testing inequality)
1 && 0 % 0 (AND operation)
1 || 0 % 1 (OR operation)

% Variable Assignment
a = 3 % set a equal to 3
a = 3; % set a equal to 3 and suppress printing
b = "hi" % string assignment
c = (3 >= 1) % set c equal to 1 because this statement is true
a = pi; % set a equal to the number pi
a % prints off the value of a as it would in variable assignment with no ";"
disp(a) % just print off the number a, don't list variable name 
disp(sprintf('2 decimals: %0.2f', a)) % C like printing of a to 100th place
disp(sprintf('6 dcmls: %0.6f', a)) % prints to the 6th decimal place
format long % default environment to printing extra digits
a
format short % default environment to printing less digits
a

% Matrices in Octave
% Matrices in Octave are created row wise, with a ";" indicating a new row
a = [1 2 ; 3 4 ; 5 6] % creates a 3 by 2 matrix
v = [1 2 3] % 1 by 3 matrix (3 dimensional row vector)
v = 1:6 % 6 dimensional row vector, 1 to 6 (step defaults to 1)
v = 1:0.1:2 % 11 element row vector (1 by 11 matrix), 0.1 steps from 1 to 2 
v = [1; 2; 3] % 3 by 1 matrix (3 dim column vector)
ones(2, 3) % shortcut to get a 2 by 3 matrix of 1s 
c = 2 * ones(2, 3) % 2 by 3 matrix of 2s (the 2 multiple is scalar mult)
w = zeros(3, 1) % 3 dimensional column vector of zeros
% eye(n) returns the n by n identity matrix (1s on diagonal, 0s elsewhere)
eye(5) % 5 by 5 identity matrix
rand(3, 3) % returns 3 by 3 matrix of Uniform[0, 1] RVs
randn(1, 3) % returns 3 dimensional row vector of Normal(mu=0, sigma=1) RVs
w = -6 + sqrt(10) * (randn(1, 10000)); % 10000 dimensional row vector of...
%...standard normals multiplied by square root of 10 and 6 subtracted 
hist(w); % histogram with default bins
hist(w, 50); % histogram with 50 bins 
% asking for help
help eye % returns help on the "eye" command

%% Moving Data Around in Octave
A = [1 2 ; 3 4 ; 5 6]
size(A) % returns a 1 by 2 matrix: 3 2, indicating A is a 3 by 2 matrix
size(A, 2) % returns the amount of columns in A (2)
length([1, 2, 3, 4]) % returns the length of the vector (4)
% length returns the larger dimension for a matrix but this is confusing
pwd % prints the current working directory
ls % list the files in the working directory
% cd <filePath> (changes the working directory to filePath) 
% load <filePath> (loads the data into a matrix, relative to the working dir)
who % lists the current Octave variable names in memory
whos % the same as who but more detail (e.g. includes size of variables)
clear A % removes the variable from the Octave workspace
% clear (with no object argument after clears every var from Octave memory)
who % A no longer exists because it was cleared
% save <fileName> <obj>; (saves object "obj" as file "fileName" in working dir)
% load <fileName> (reloads what was just saved to disk back into memory)
% save <textFileName> v -ascii (save as readable ascii formatted text file)

%% Manipulating Data Structures in Octave
% Subsetting
A = [1 2 ; 3 4 ; 5 6]
A(3, 2) % returns 6, or the 3rd row and 2nd column entry
A(2, :) % returns 2 dim row vector [3 4] (everything in 2nd row) 
A(:, 2) % returns 3 dim col vector [2; 4; 6] (everything in 2nd column) 
A([1 3], :) % returns 2 by 2 matrix [1 2 ; 5 6] (everything in 1st & 3rd row) 
% Appending
A = [1 ; 2 ; 3] % initialize A to a 3 dimensional column vector
A(:, 2) = [40; 50; 60]; % append this 3 dim col vector to 2nd column in A
A = [A, [700; 800; 900]] % append this 3 dim dim col vector to 3rd col in A 
% since the right defines the new A, we assign this new statement to A
% this contrasts the example prior where we only define the 2nd column in...
% ...our appending, so we assign it to the 2nd column of A
A(:) % columnwise collapse elements of matrix A into a single column vector
A = [1 2 ; 3 4 ; 5 6]
B = [10 11; 12 13; 14 15]
C = [A B] % append B to the right of A (analogous to "cbind" in R language)
size(C) % returns 3 by 4 (communicated via row vector)
D = [A; B] % append B to the bottom of A (analogous to "rbind" in R language)
size(D) % returns 6 by 2

%% Computational Operations on Data in Octave
% initialize some matrices for computation to be performed on
A = [1 2 ; 3 4 ; 5 6];
B = [11 12; 13 14; 15 16];
C = [1 1; 2 2];
% matrix multiplication is the default in Octave (number of cols in left...
% ...operand must have same amount of rows as right operand)
A * C % 3 by 2 matrix bimes 2 by 2 matrix returns 3 by 2 matrix
% element wise multiplication is same as matrix except "*" is prefaced by a "."
A .* B % dimensions of A & B must be equal and operation is commutative
% scalar division can occur by replacing "*" with "/" in operation
1 ./ A % returns inverse of every element in A
log(A) % take the natural log of every element in A
exp(A) % take the exponential of every element in A
abs(A) % element wise absolute value of entries in A
-A % returns the negative of every element in A
% uniform element wise addition occurs when a single scalar is added to a matrix
[1 2; 3 4; 5 6] + 1 % adds 1 to every element in left operand
A' % using the "'" transposes matrix A
(A')' % returns the original A because of a double transpose
a = [1 15 0.5 2]
max(a) % returns the maximum value of 15
max(rand(3), rand(3)) % returns element wise max of two 3 dim random matrices
[val, ind] = max(a) % returns the (value, index) of maximum value: (15, 2)
a < 3 % returns a same dimensional matrix as a with 1s if element is less...
% ...than 3, 0 otherwise
sum(a) % returns 18.5, or the sum of the vector
prod(a) % returns 15, or the product of all elements in the vector
floor(a) % rounds down each element to the nearest integer
ceil(a) % rounds each element up to the nearest integer
find(a < 3) % returns the indices of the elements less than 3
X = magic(3) % returns a 3 dim "magic" matrix (all diags, rows & cols sum...
% ...to same value
[r, c] = find(X >= 7) % returns corresponding row/col coordinates where the...
% ...entry is greater than or equal to 7
max(X, [], 1) % returns the maximum of each column
max(X, [], 2) % returns the maximum per each row
max(X) % defaults to column wise maximum
max(max(X)) % returns maximum of the entire matrix
max(X(:)) % returns max of the entire matrix by collapsing X into column vector
X = magic(9)
sum(X, 1) % does a column wise sum
sum(X, 2) % does a row wise sum
sum(sum(X .* eye(9))) % summation of main diagonal
X = magic(3)
inv = pinv(X) % calculates the inverse matrix of X
X * inv % returns the identity matrix

%% Plotting in Octave 
t = [0:0.01:0.98]; % create a 99 element row vector from 0 to 0.98 step 0.01
y1 = sin(2 * pi * 4 * t); % 99 element row vector of t with sin transformation
plot(t, y1) % plot y1 as a function of t [syntax: plot(x, y)]
y2 = cos(2 * pi * 4 * t); % cosine transformation to each of 99 entries
plot(t, y2); % this second call to plot overwrites the 1st, need "hold on"
hold on;
plot(t, y1, 'r'); % color the sin curve red
% set axes labels
xlabel('Time')
ylabel('Value')
legend('cos', 'sin')
title('Hello, World! Plot')
close % close down the plot (comment out to show plot)
% plot 2 plots in 2 different windows
figure(1); plot(t, y1);
figure(2); plot(t, y2);
close 
close % comment these out to show 1 or 2 plots 
subplot(1, 2, 1) % take a 1 by 2 grid and plot in the first entry
plot(t, y1) % plot in the first part of the array
subplot(1, 2, 2) % take a 1 by 2 grid and plot in the second entry
plot(t, y2) % plot in the second part of the array
axis([0.5 1 -1 1]) % 2nd plot has x axis ranging from 0.5 to 1, y from -1 to 1
clf % another way for "close" (comment out to examine above plot)
% Octave uses comma chaining, meaning that multiple commands can be on the...
% ...same line if separated by a "," (if separated by ";", does not print calls)

%% Control Statements
% conditional code
v = zeros(10, 1) % 10 dim col vector of zeros
v(1) = 2;
if v(1) == 1,
    disp('the value is one');
elseif v(1) == 2, 
    disp('the value is two');
else,
    disp('the value is neither one nor two');
end; 

% For Loops
v = zeros(10, 1) % 10 dim col vector
for i = 1:10,
    % square each index and input at that index
    v(i) = 2 ^ i
end;
% indenting does not matter in Octave loops besides readability
% in a loop, "break" means to exit the loop while "continue" means to...
% ...go onto the next iteration (identical to Python)

% While Loops
i = 1;
while i <= 5,
    v(i) = 100; % set element equal to 100 so long as its index is <= 5
    i = i + 1;
end;
disp(v)

i = 1;
while true,
    v(i) = 999;
    i = i + 1;
    % leave the while loop if the index is the sixth one
    if i == 6,
        break
    end;
end;
v

% Functions
function y = squareThisNumber(x)
    % just square the input x and set equal to return value y 
    y = x ^ 2;
endfunction 
% apply the above function
y1 = squareThisNumber(5) % returns 25
% Octave functions can return multiple values
function [y1, y2] = squareAndCubeThisNumber(x)
    y1 = x ^ 2
    y2 = x ^ 3
endfunction
[a, b] = squareAndCubeThisNumber(5) % sets a equal to the function's 1st...
% ...output (y1 - squared) & b equal to the function's 2nd output (y2 - cubed)

%% Vectorization
% Vectorization is the art of converting operations that normally would be...
% ...done via a for loop into a matrix algebra formatted execution
% Example - find the dot product of the following two column vectors
theta = [1; 3; .2]; x = [7; 6; 5];
% Unvectorized (suboptimal)
prediction = 0; 
for i = 1:size(theta),
    prediction = prediction + theta(i) * x(i);
end;
disp(prediction)
% Vectorized (optimal)
prediction = theta' * x % just treat this like a matrix operation to get the...
% ...dot product using built in optimized matrix algebra Octave capabilities!
























































































