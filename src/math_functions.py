from math import sqrt
from typing import List


def pgcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor (GCD) of a, b

    Args:
        a (int): A positive integer number
        b (int): A positive integer number

    Returns:
        int: Returns the greatest common divisor (GCD)
    """
    while b > 0:
        a, b = b, a % b

    return a


def integer_digits(n: int) -> int:
    """List of digits of n

    Args:
        n (int): A positive integer number

    Returns:
        int: Return the list of digits of a given integer
    """
    l = []
    while n != 0:
        l.append(n % 10)
        n //= 10
    return l

    """Counts the number of digits of an integer

    Args:
        n (int): A positive integer number

    Returns:
        int: Return the number of digits
    """
    return len(integer_digits(n))


def all_dividers(n: int) -> List:
    """Generate the list of all dividers of n

    Args:
        n (int): A positive integer number

    Returns:
        List: all dividers of n
    """
    l: list = [1, n]
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            l.append(i)
    return l


def is_prime(n: int) -> bool:
    """Verify if the number given in parameter is a prime number

    Args:
        n (int): A positive integer number

    Returns:
        bool: Return True if prime False otherwise
    """
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(sqrt(n)) + 1))


def is_perfect(n: int) -> bool:
    """Verify if a given integer is a perfect number (a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself)

    Args:
        n (int): A positive integer number

    Returns:
        bool: Return True if n is a perfect number False otherwise
    """
    return (sum(all_dividers(n)) - n) == n


def is_friend(a: int, b: int) -> bool:
    """Verify if a, b are friends number (Two numbers a, b are friends then
        - the sum of dividers excluding the a itself is equal to b
        - the sum of dividers excluding the b itself is equal to a)

    Args:
        a (int): A positive integer number
        b (int): A positive integer number

    Returns:
        bool: Return True if a & b are friends number False otherwise
    """
    return (sum(all_dividers(a)) - a) == b and (sum(all_dividers(b)) - b) == a


def is_lucky(n: int) -> bool:
    """[summary]

    Args:
        n (int): A positive integer number

    Returns:
        bool: [description]
    """
    pass


def fibonacci(n: int) -> int:
    """Calculate the fibonacci's terms using Binet formula
        1/√5 * (ɸ^n - ɸ'^n)

    Args:
        n (int): A positive integer number

    Returns:
        int: The nth term of the Fibonacci sequence
    """
    phi = (1 + sqrt(5)) / 2
    phi_prime = (1 - sqrt(5)) / 2
    return int((1 / sqrt(5)) * (phi ** n - phi_prime ** n))


def lucas(n: int) -> int:
    """Calculate the lucas's terms using Binet formula
      Ln = Fn-1 + Fn+1

    Args:
        n (int): A positive integer number

    Returns:
        int: The nth term of the Fibonacci sequence
    """
    return fibonacci(n - 1) + fibonacci(n + 1)


if __name__ == "__main__":
    # print(all_dividers(1024))
    # print([x for x in range(32000) if is_prime(x)])
    # n = 3647895269988
    # print(integer_digits(n))
    # print(n)
    # print(count_digits(n))
    # print(pgcd(360, 48))
    # for i in range(72):
    #     print(fibonacci(i), end=" -> ")

    # print([lucas(k) for k in range(50)])
    primes = [p for p in range(2, 400_001) if is_prime(p)]
    print(len(primes))
