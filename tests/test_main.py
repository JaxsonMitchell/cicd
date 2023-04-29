"""
Test the main module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from main import is_prime, is_prime_str


def test_is_prime():
    assert not is_prime(4)
    assert is_prime(31)
    assert not is_prime(1)


def test_is_prime_str():
    assert is_prime_str("7") == "7 is prime."
    assert is_prime_str("4") == "4 is composite."
    assert is_prime_str("1") == "1 is composite."
    assert is_prime_str("-1") == "Please enter a number."
    assert is_prime_str("A") == "Please enter a number."
    assert is_prime_str("") == "Please enter a number."
