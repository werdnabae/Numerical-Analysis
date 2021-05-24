A = randn(32);
A2 = A * 5 + 1;
B = inv(A);
AB = A*B;
e = eig(A);  

% A = [2, 1, -1;
%     -3, -1, 2;
%     -2, 1, 2];
% B = [8; -11; -3];
% X = linsolve(A, B); % can solve system of matrix using linsolve
% Ap = inv(A);
% Xp = Ap*B; % can solve system of matrix using the inverse
% Xi = A\B; % can solve using this

% for solving sparse matrix, define: A = sparse(A). b = sparce(b). x = A/b