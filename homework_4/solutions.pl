% PART 1

parent(bart,homer). 
parent(bart,marge). 
parent(lisa,homer). 
parent(lisa,marge). 
parent(maggie,homer). 
parent(maggie,marge). 
parent(homer,abraham). 
parent(herb,abraham). 
parent(tod,ned). 
parent(rod,ned). 
parent(marge,jackie). 
parent(patty,jackie). 
parent(selma,jackie). 
female(maggie). 
female(lisa). 
female(marge). 
female(patty). 
female(selma). 
female(jackie). 
male(bart).  
male(homer). 
male(herb). 
male(burns). 
male(smithers). 
male(tod). 
male(rod). 
male(ned). 
male(abraham). 

brother(X, Y) :- parent(X, Z), parent(Y, Z), male(Y), X \= Y.
sister(X, Y) :- parent(X, Z), parent(Y, Z), female(Y), X \= Y.
aunt(X, Y) :- parent(X, Z), sister(Z, Y) .
uncle(X, Y) :- parent(X, Z), brother(Z, Y).
grandfather(X, Y) :- parent(X, Z), parent(Z, Y), male(Y).
granddaughter(X, Y) :- parent(Y, Z), parent(Z, X), female(Y).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(Z, Y), ancestor(X, Z).


% PART 2

occupation(joe,oral_surgeon). 
occupation(sam,patent_lawyer). 
occupation(bill,trial_lawyer). 
occupation(cindy,investment_banker). 
occupation(joan,civil_lawyer).
occupation(len,plastic_surgeon). 
occupation(lance,heart_surgeon). 
occupation(frank,brain_surgeon). 
occupation(charlie,plastic_surgeon). 
occupation(lisa,oral_surgeon). 
 
job(X, surgeon) :- occupation(X, oral_surgeon).
job(X, surgeon) :- occupation(X, plastic_surgeon).
job(X, surgeon) :- occupation(X, heart_surgeon).
job(X, surgeon) :- occupation(X, brain_surgeon).
job(X, lawyer) :- occupation(X, patent_lawyer).
job(X, lawyer) :- occupation(X, trial_lawyer).
job(X, lawyer) :- occupation(X, civil_lawyer).

address(joe,houston). 
address(sam,pittsburgh). 
address(bill,dallas). 
address(cindy,omaha). 
address(joan,chicago). 
address(len,college_station). 
address(lance,los_angeles). 
address(frank,dallas). 
address(charlie,houston). 
address(lisa,san_antonio). 

lives(X, california) :- address(X, los_angeles).
lives(X, texas) :- address(X, houston).
lives(X, texas) :- address(X, dallas).
lives(X, texas) :- address(X, college_station).
lives(X, texas) :- address(X, san_antonio).

salary(joe,50000). 
salary(sam,150000). 
salary(bill,200000). 
salary(cindy,140000). 
salary(joan,80000). 
salary(len,70000). 
salary(lance,650000). 
salary(frank,85000). 
salary(charlie,120000). 
salary(lisa,190000). 

salary_enough(X) :- salary(X, Y), Y > 100000.
query2a(X) :- job(X, lawyer).
query2b(X) :- job(X, surgeon), lives(X, california).
query2c(X) :- job(X, surgeon), lives(X, texas), salary_enough(X).


% PART 3

subject(algebra,math).
subject(calculus,math).
subject(dynamics,physics).
subject(electromagnetism,physics).
subject(nuclear,physics).
subject(organic,chemistry).
subject(inorganic,chemistry).
degree(bill,phd,chemistry).
degree(john,bs,math).
degree(chuck,ms,physics).
degree(susan,phd,math).
retired(bill).

canTeach(X, Y) :- degree(X, phd, Z), subject(Y, Z).
canTeach2(X, Y) :- degree(X, phd, Z), subject(Y, Z), \+ retired(X).
canTeach3(X, Y) :- degree(X, phd, Z), subject(Y, Z), \+ retired(X).
canTeach3(X, Y) :- degree(X, ms, Z), subject(Y, Z), \+ retired(X).


% PART 4

bit(X) :- member(X, [0, 1]).
octal_code(A, B, C) :- bit(A), bit(B), bit(C), format('~w~w~w~n',[A,B,C]).


% PART 5

color(red).
color(blue).
color(green).

mapcolor(WA, NT, SA, Q, NSW, V, T) :- color(WA), color(NT), color(SA), color(Q), color(NSW), color(V), color(T),
WA \= NT, WA \= SA,
NT \= WA, NT \= color(SA), color(NT) \= color(Q),
color(SA) \= color(WA), color(SA) \= color(NT), color(SA) \= color(Q),
color(Q) \= color(NT), color(Q) \= color(SA), color(Q) \= color(NSW),
color(NSW) \= color(Q), color(NSW) \= color(SA), color(NSW) \= color(V),
color(V) \= color(NSW), color(V) \= color(SA).
