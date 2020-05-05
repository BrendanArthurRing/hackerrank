# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/

def runner_up(n, arr):
    """
    Given an integar total of scores n,
    and given a list of scores arr:
    1. Find the 2nd greatest score, aka the runner up.
    >>> n = 5
    >>> arr = [2, 3, 6, 6, 5]
    >>> runner_up(n, arr)
    5

    """
    scores = list(enumerate(sorted(set(arr), reverse=True)))
    print(scores[1][1])

    return scores[1][1]

assert runner_up(5, [2, 3, 6, 6, 5]), 5