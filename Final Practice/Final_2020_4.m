clear, clc
A = randn(4096);

u= ones(4096, 1); % The initial choice of eigenvector.
n=length(u); % Size of initial eigenvector.
v=zeros(n,1);
eps=0.001; %error of tolerance
err=10;m1=1;m2=1;
 while err>eps  %Calculating the greatest eigenvalue and the corresponding eigenvector.
   v=A*u; 
   m2=max(abs(v));
   u=v/m2;
   err=abs(m1-m2);
   m1=m2;
 end

% m1 is the dominant eigenvalue
% u is the dominant eigenvector

%got code from Monotosh Mandal: 
%https://www.mathworks.com/matlabcentral/fileexchange/72587-power-method-to-find-dominant-eigenvalue?s_tid=mwa_osa_a

y = [0 0 0 0 0 0 0];
for i = 1:4096
    for j = 1:4096
        if A(i, j) < -1
            y(1) = y(1) + 1;
        end
        if (A(i, j) > -1) && (A(i, j) < -0.5)
            y(2) = y(2) + 1;
        end
        if (A(i, j) > -.5) && (A(i, j) < -0.25)
            y(3) = y(3) + 1;
        end
        if (A(i, j) > -.25) && (A(i, j) < 0.25)
            y(4) = y(4) + 1;
        end
        if (A(i, j) > 0.25) && (A(i, j) < 0.5)
            y(5) = y(5) + 1;
        end
        if (A(i, j) > 0.5) && (A(i, j) < 1)
            y(6) = y(6) + 1;
        end
        if (A(i, j) > 1) 
            y(7) = y(7) + 1;
        end
    end
end

bar(y)
% edges = [-5, -1, -.5, -.25, .25, 0.5, 1, 5];
% h = histogram(A, edges);
% h.Normalization = 'countdensity';