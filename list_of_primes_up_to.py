# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 02/17/2025
# Description: list of primes

def list_of_primes_up_to(limit=100):
    # Create a list where True represents a prime number
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    # Start eliminating non-prime numbers
    for num in range(2, int(limit ** 0.5) + 1):
        if primes[num]:  # If num is still marked as prime
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False  # Mark multiples as non-prime

    # Return a list of prime numbers
    return [i for i, is_prime in enumerate(primes) if is_prime]
