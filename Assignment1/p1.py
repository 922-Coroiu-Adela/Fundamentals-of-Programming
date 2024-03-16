"""
3. For a given natural number n find the minimal natural number m formed with the same digits. (e.g. n=3658, m=3568).
"""

def get_frequncies(n):
    """
    Returns a dictionary with the frequencies of each digit in n.
    """
    freq = {}
    for i in range(0,10):
        freq[i] = 0
    while n != 0:
        freq[n % 10] += 1
        n = n // 10
    return freq

def get_minimal(n):
    """
    Returns the minimal number formed with the same digits as n.
    """
    freq = get_frequncies(n)
    m = 0
    # The minimal number can't start with 0.
    if freq[0] != 0:
        poz = 1
        while freq[poz] == 0:
            poz += 1
        while freq[poz] != 0:
            freq[poz] -= 1
            m = m * 10 + poz
        while freq[0] != 0:
            freq[0] -= 1
            m = m * 10
    for i in range(1,10):
        while freq[i] != 0:
            freq[i] -= 1
            m = m * 10 + i
    return m

if __name__ == "__main__":
    while True:
        n = int(input("n = "))
        print(get_minimal(n))

