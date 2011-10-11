% What is the smallest number divisible by each of the numbers 1 to 20?

% 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
% What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?

-module(e005).
-export([
    main/1
]).

divisible(N) ->
    divisible(N, N, 1).
divisible(_, C, X) when C == 1 ->
    X;
divisible(N, C, X) ->
    if
        X rem C == 0 ->
            divisible(N, C - 1, X);
        true ->
            divisible(N, N, X + 1)
    end.

main(_) ->
    io:format("Smallest number divisible by 1 to 10: ~w~n", [divisible(10)]),
    io:format("Smallest number divisible by 1 to 10: ~w~n", [divisible(20)]).
