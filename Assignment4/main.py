# problems 1 and 1

"""
1. A number of n coins are given, with values of a1, ..., an and a value s. Display all
payment modalities for the sum s. If no payment modality exists print a message.
Implement the algorithm using backtracking (implement both an iterative and a recursive algorithm)
"""

def print_solutions(solutions):
    if len(solutions) == 0:
        print("No payment modality exists")
    else:
        print("Payment modalities:")
        for solution in solutions:
            print(solution)

# the complexity of the algorithm is O(2^n), (the 2 is because we have 2 branches for each coin - we can include it or not
# and the n is because we have n coins)
def finding_payment_modality_recursive(coins, target_sum):
    def backtracking(start, current_sum, current_solution):
        if current_sum == target_sum:
            solutions.append(current_solution[:])
        if current_sum > target_sum:
            return
        for i in range(start, len(coins)):
            current_solution.append(coins[i])
            backtracking(i + 1, current_sum + coins[i], current_solution)
            current_solution.pop()

    solutions = []
    backtracking(0, 0, [])

    print_solutions(solutions)

# the complexity of the algorithm is O(2^n), (the 2 is because we have 2 branches for each coin - we can include it or not
# and the n is because we have n coins)
def finding_payment_modality_iterative(coins, target_sum):
    solutions = []
    stack = []
    stack.append(([], 0, 0))
    while stack:
        current_solution, current_sum, start = stack.pop()
        if current_sum == target_sum:
            solutions.append(current_solution[:])
        if current_sum > target_sum:
            continue
        for i in range(start, len(coins)):
            new_solution = current_solution + [coins[i]]
            new_sum = current_sum + coins[i]
            stack.append((new_solution, new_sum, i + 1))

    print_solutions(solutions)

def read_input():
    f = open("input.txt", "r")
    coins = []
    n = int(f.readline())
    coins = [int(x) for x in f.readline().split()]
    target_sum = int(f.readline())
    f.close()
    return coins, target_sum

def main():
    coins, target_sum = read_input()
    print("Recursive algorithm: ")
    finding_payment_modality_recursive(coins, target_sum)
    print("Iterative algorithm: ")
    finding_payment_modality_iterative(coins, target_sum)

if __name__ == "__main__":
    main()
