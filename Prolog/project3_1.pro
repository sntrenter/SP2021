%male, female, parent. Then add rules such as sister, brother, sibling, father, mother, grandparent

%male/female recorded left to right top to bottom
%male

male(pete).
male(mark).
male(tom).
male(john).
male(frank).
male(matt).
male(henry).
male(todd).

%female

female(anne).
female(lilly).
female(kate).
female(alice).
female(jenny).

% parent = parent(child,parent)
%recorded bottom up, r->l
parent(henry,alice).
parent(jenny,matt).
parent(todd,matt).
parent(lilly,mark).
parent(john,mark).
parent(frank,mark).
parent(kate,tom).
parent(alice,anne).
parent(matt,anne).
parent(mark,pete).
parent(tom,pete).
parent(anne,pete).

% is X a sister/brother to Y
sister(X,Y):- female(X),parent(X,P),parent(Y,P),X\=Y.
brother(X,Y):- male(X),parent(X,P),parent(Y,P),X\=Y.
sibling(X,Y) :- parent(X,P),parent(Y,P),X\=Y.

%father, mother, grandparent
%X is the father/mother of Y
father(X,Y) :- male(X), parent(Y,X).
mother(X,Y) :- female(X), parent(Y,X).
%grandparent x is the grandparent of y
grandparent(X,Y) :- parent(Y,Z),parent(Z,X).


%(a) Is Pete Mark’s parent?  
% parent(pete,X),parent(mark,X). = false
% (b) Is Anne Jenny’s parent?
% parent(anne,X),parent(jenny,X). = false
%(c) Who is Todd’s father? 
% father(X,todd). = matt
%(d) Who is Tom’s sibling?
% sibling(X,tom). = mark  anne
% (e) Who is Lilly’s brother?
% brother(X,lilly). = john frank
% (f) Who is Henry’s grandparent?
% grandparent(X,henry). = anne
% (g) Who is Alice’s sister? 
% sister(X, alice). = false
%(h)  Is Frank Kate’s brother?
% brother(X,frank),brother(X,kate). = false
% (i) Who is Matt’s mother? 
%mother(X,matt). = anne
%(j) Is Mark Anne’s brother?
%brother(X,mark),brother(X,anne). = tom