% Find the largest prime factor of a composite number.

% The prime factors of 13195 are 5, 7, 13 and 29.
% What is the largest prime factor of the number 600851475143 ?

-module(e003).
-export([
    main/1,
    pfactor/1
]).

pfactor(N) ->
    pfactor_(N, []).
pfactor_(N, F) ->
    Next = pfactor_next(N, 2),
    if
        Next == N ->
            [N | F];
        true ->
            pfactor_(trunc(N / Next), [Next | F])
    end.

pfactor_next(N, Factor) ->
    if
        Factor == N ->
            Factor;
        N rem Factor == 0 ->
            Factor;
        true ->
            pfactor_next(N, Factor + 1)
    end.


main(_) ->
    io:format("Prime Factors of 13195: ~w~n", [pfactor(13195)]),
    io:format("Prime Factors of 600851475143: ~w~n", [pfactor(600851475143)]).
