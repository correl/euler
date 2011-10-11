% Add all the natural numbers below one thousand that are multiples of 3 or 5.

% If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
% Find the sum of all the multiples of 3 or 5 below 1000.

-module(e001).
-export([
    main/1
    ]).

sum(3) ->
    0;
sum(Max) ->
    N = Max - 1,
    if
        N rem 3 == 0 ->
            A = N;
        N rem 5 == 0 ->
            A = N;
        true ->
            A = 0
    end,
    sum(N) + A.

main(_) ->
    io:format("Sum of <   10: ~w~n", [sum(10)]),
    io:format("Sum of < 1000: ~w~n", [sum(1000)]).
