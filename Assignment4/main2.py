"""
1. Determine the longest common subsequence of two given sequences. Subsequence elements are not required to occupy
consecutive positions. For example, if X = "MNPNQMN" and Y = "NQPMNM", the longest common subsequence has length 4,
and can be one of "NQMN", "NPMN" or "NPNM". Determine and display both the length of the longest common subsequence
as well as at least one such subsequence.
"""


# The naive approach uses recursion to explore all possible subsequences (it has an exponential time complexity,
# making it inefficient for long input sequences).

def longest_common_subsequence_naive(X, Y):
    def helper(i, j): # the function calculates the lcs of the first i elements of X and the first j elements of Y
        if i == 0 or j == 0: # the case where one of the sequences is empty
            return ""
        if X[i - 1] == Y[j - 1]: # if the last elems of the sequences are equal, we add them to the lcs
            return helper(i - 1, j - 1) + X[i - 1]
        else:
            lcs1 = helper(i - 1, j) # we try to find the lcs of the first i - 1 elements of X and the first j elements of Y
            lcs2 = helper(i, j - 1) # we try to find the lcs of the first i elements of X and the first j - 1 elements of Y
            return lcs1 if len(lcs1) > len(lcs2) else lcs2

    lcs = helper(len(X), len(Y))
    return len(lcs), lcs


def longest_common_subsequence_dynamic_programming(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)] # making a matrix

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from the dp table
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs = "".join(reversed(lcs))
    return dp[m][n], lcs

def main_function():
    while True:
        print("1. Naive approach")
        print("2. Dynamic programming")
        print("0. Exit")
        option = input("Enter option: ")
        if option == "1":
            X = input("Enter the first sequence: ")
            Y = input("Enter the second sequence: ")
            length, lcs = longest_common_subsequence_naive(X, Y)
            print("Length of LCS:", length)
            print("One such LCS:", lcs)
        elif option == "2":
            X = input("Enter the first sequence: ")
            Y = input("Enter the second sequence: ")
            length, lcs = longest_common_subsequence_dynamic_programming(X, Y)
            print("Length of LCS:", length)
            print("One such LCS:", lcs)
        elif option == "0":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main_function()





