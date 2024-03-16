"""
15. Generate the largest perfect number smaller than a given natural number n. If such a number does not exist,
a message should be displayed. A number is perfect if it is equal to the sum of its divisors, except itself.
(e.g. 6 is a perfect number, as 6=1+2+3).
"""

def get_divisors(n):
    """
    Returns a list with the divisors of n.
    """
    div = []
    for i in range(1,n):
        if n % i == 0:
            div.append(i)
    return div

def get_sum(div):
    """
    Returns the sum of the elements in div.
    """
    s = 0
    for i in div:
        s += i
    return s

def get_largest(n):
    """
    Returns the largest perfect number smaller than n.
    """
    for i in range(n-1,0,-1):
        div = get_divisors(i)
        s = get_sum(div)
        if s == i:
            return i
    return "There is no such number."

if __name__ == "__main__":
    while True:
        n = int(input("n = "))
        print(get_largest(n))
