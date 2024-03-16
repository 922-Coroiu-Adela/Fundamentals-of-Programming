"""
for A2: bubble sort si gnome sort

Implement a menu-driven console application to help visualize the way sorting algorithms work.
You will be given two of the algorithms from the list below to implement (one from each set).
When started, the program will print a menu with the following options:

Generate a list of n random natural numbers. Generated numbers must be between 0 and 100.
Sort the list using the first algorithm - bubble sort
Sort the list using the second algorithm - gnome sort
Exit the program

Before starting each sort, the program will ask for the value of parameter step. During sorting, the program
will display the partially sorted list on the console each time it makes step operations or passes,
depending on the algorithm (e.g., if step=2, display the partially sorted list after each 2 element swaps
in bubble sort, after each 2 element insertions in insert sort, after every 2nd generation of a permutation
in permutation sort etc.).

"""

from random import randint

def generateList():
    list = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        list.append(randint(0, 100))
    return list

def bubbleSort(list, step):
    n = len(list)
    s = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                s += 1
            if s % step == 0:
                print(list)
    print(list)


def gnomeSort(list, step):
    n = len(list)
    s = 0
    index = 0
    while index < n:
        if index == 0:
            index += 1
        if list[index] >= list[index-1]:
            index += 1
        else:
            list[index], list[index-1] = list[index-1], list[index]
            index -= 1
            s += 1
        if s % step == 0:
            print(list)
    print(list)


def main():
    list = []
    while True:
        print("1. Generate a list of n random natural numbers. Generated numbers must be between 0 and 100.")
        print("2. Sort the list using the first algorithm - bubble sort")
        print("3. Sort the list using the second algorithm - gnome sort")
        print("4. Exit the program")
        option = input("Choose an option: ")
        if option == "1":
            list = generateList()
            print(list)
        elif option == "2":
            step = int(input("Enter the step: "))
            bubbleSort(list, step)
        elif option == "3":
            step = int(input("Enter the step: "))
            gnomeSort(list, step)
        elif option == "4":
            break
        else:
            print("Invalid option!")

main()