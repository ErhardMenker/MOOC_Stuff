%%% Dimensionality Reduction

%% Dimensionality Reduction Motivation
% If 2 variables are highly correlated, they can be collapsed to 1 dimension
% Dimensionality reduction works by breaking data into its projection
% Data can be plotted with dimensionality reduction by assigning meanings to...
% ...the collapsed variables

%% Principal Component Analysis Overview
% PCA is the most common dimensionality reduction algorithm
% PCA tries to minimize the projection of a lower dimensional vector (k) on...
% ...the n dimensional data such that k < n (min projection -> lowest error)
% Example: PCA could fit a plane to 3 dimensional data 
% PCA is not linear regression - linear regression minimizes the sum of...
% ...errors squared (vertical distance) while PCA minimizes the points'...
% ...projections (the orthogonal connection between the point & fitted...
% ...subspace)
% PCA has no "special" outcome variable y that is trying to be predicted
% PCA expresses the value of the variables as linear projections of the others
% Example: if you have 3 dimensional data, then knowing x1 & x2 is sufficient...
% ...information to ascertain the projected value of x3 from PCA

%% PCA Algorithm
% Execute preprocessing by feature scaling & mean normalization for each feature
% Compute the singular value decomposition (SVD) of the covariance matrix's...
% ...Eigenvectors, resulting in an n by n matrix (for k element PCA, extract...
% ...the first k vectors of this matrix)

%% PCA Application
% Choose the smallest # of K such that 99% of variance is retained
% For many datasets, K can be quite small to retain 99% of variance because...
% ...features are highly correlated
% PCA can be used to engineer new features that are used in a supervised...
% ...ML algorithm to speed up its execution
% PCA should only be executed on the training set, then tested on the CV set
% A poor use of PCA is to try to prevent overfitting; use regularization instead
% Try running an ML algorithm without PCA (for a supervised algorithm); only...
% ...if this is prohibitively slow, use PCA




