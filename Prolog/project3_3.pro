%Write a Prolog program that returns a list containing a union of the elements of two given sets.


union([],[],[]).
union(list,[],list).
union(list, [head|tail], [head|Output]):- \+(member(head,list)), union(list,tail,Output).
union(list, [head|tail], Output):- member(head,list), union(list,tail,Output).  

% union([3,r,c,d,f], [3,4,5,t,6,j], X).
% [4, 5, t, 6, j, 3, r, c, d, f]