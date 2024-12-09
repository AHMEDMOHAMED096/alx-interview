#!/usr/bin/python3
"""Prime Game"""


def is_prime(num):
    """Check if a number is prime"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def remove_multiples(prime, nums):
    """Remove multiples of a given prime number from a list"""
    return [num for num in nums if num % prime != 0]


def play_game(n):
    """
    Simulate a game between Maria and Ben with numbers from 1 to n"""
    nums = list(range(1, n + 1))
    turn = 0
    while True:
        primes = [num for num in nums if is_prime(num)]
        if not primes:
            return "Ben" if turn == 0 else "Maria"
        prime = primes[0]
        nums = remove_multiples(prime, nums)
        turn = 1 - turn


def isWinner(x, nums):
    """
    Determine the winner of each game and the overall winner"""
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
