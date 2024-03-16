"""
10. The palindrome of a number is the number obtained by reversing the order of its digits (e.g.
the palindrome of 237 is 732). For a given natural number n, determine its palindrome.
"""

def get_palindrome(n):
    """
    Returns the palindrome of n.
    """
    p = 0
    while n != 0:
        p = p * 10 + n % 10
        n = n // 10
    return p

if __name__ == "__main__":
    while True:
        n = int(input("n = "))
        print(get_palindrome(n))