"""
odd/even number checker
Author: Wolf Paulus (https://wolfpaulus.com)
"""


def is_prime(num: int) -> bool:
    """Return True if num is prime, False otherwise."""
    if num > 1:
        for val in range(2, int(num ** 1/2) + 1):
            if num % val == 0:
                return False
        return True
    else:
        if num == 1:
            return False
        return False


def is_prime_str(num: str) -> str:
    """Return a string indicating whether num is prime or composite."""
    if num.isnumeric():
        if int(num) == 1 or int(num) == 0:
            return f"{num} is wacc"
        return f"{num} is {'prime' if is_prime(int(num)) else 'composite'}."
    else:
        return "Please enter a number."
