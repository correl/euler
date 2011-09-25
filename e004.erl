% Find the largest palindrome made from the product of two 3-digit numbers.

% A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
% Find the largest palindrome made from the product of two 3-digit numbers.

-module(e004).
-export([
    main/1
]).

product(Min, Max) ->
    product(Min, Max, Max, Max, 0).
product(Min, _, N1, _, Product) when N1 < Min ->
    Product;
product(Min, Max, N1, N2, Product) when N2 < Min ->
    product(Min, Max, N1 - 1, Max, Product);
product(Min, Max, N1, N2, Product) ->
    P = trunc(N1 * N2),
    S = integer_to_list(trunc(N1 * N2)),
    R = lists:reverse(S),
    if
        S == R, P > Product ->
            product(Min, Max, N1, N2 - 1, P);
        true ->
            product(Min, Max, N1, N2 - 1, Product)
    end.

main(_) ->
    io:format("Largest palindrome product of 2-digit numbers: ~w~n", [product(10, 99)]),
    io:format("Largest palindrome product of 3-digit numbers: ~w~n", [product(100, 999)]).
