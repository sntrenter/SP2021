%Write a Prolog program that finds the maximum of a list of numbers. 
%Submission file should include a screenshot with tracing a program execution when a
% list only has 2 members and execution without tracing when a list has 8 elements. 


maxinlist([X],X).

maxinlist([H|T],Max):-maxinlist(T,Max),H @< Max.
maxinlist([Max|T],Max):- maxinlist(T,M),M @< Max.


% maxinlist([20,2000,6,8,17,22,48,77,98,152],X).
% 2000

% maxinlist([20,6],X).
% 20
