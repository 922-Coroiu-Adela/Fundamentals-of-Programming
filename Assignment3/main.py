"""
for A2: bubble sort si gnome sort
Let's say that as part of A2 you've implemented BubbleSort and ShellSort. Let's say the user wishes to see
the behaviour of these algorithms in the worst case. Your program will generate five lists (e.g., lenghts 500,
1000, 2000, 4000 and 8000 elements) in which elements are in worst case configuration (for bubble sort, this
happens if the list is already sorted, but in reverse). Then, you will time how long it takes to sort each list
using a module such as timeit, and display the results on the console.
In case the algorithm takes too long/little, you can adjust the list lenghts (e.g., permutation sort)
Make sure that all calls to the sorting algorithms use the same input lists.
Make sure the sorting algorithms do not perform additional work (e.g., displaying on the console, as required
 for A2)
Display the results (list length, sort duration) in a way that allows users to see the progression of the runtime.

"""

from random import randint
import string
import timeit

def generateList():
    list = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        list.append(randint(0, 100))
    return list

def generateList500(type_of_case: string):
    list = []
    if type_of_case == "best":
        for i in range(500):
            list.append(i)
    elif type_of_case == "worst":
        for i in range(500, 0, -1):
            list.append(i)
    elif type_of_case == "average":
        for i in range(500):
            list.append(randint(0, 500))
    return list

def generateList1000(type_of_case: string):
    list = []
    if type_of_case == "best":
        for i in range(1000):
            list.append(i)
    elif type_of_case == "worst":
        for i in range(1000, 0, -1):
            list.append(i)
    elif type_of_case == "average":
        for i in range(1000):
            list.append(randint(0, 1000))
    return list

def generateList2000(type_of_case: string):
    list = []
    if type_of_case == "best":
        for i in range(2000):
            list.append(i)
    elif type_of_case == "worst":
        for i in range(2000, 0, -1):
            list.append(i)
    elif type_of_case == "average":
        for i in range(2000):
            list.append(randint(0, 2000))
    return list

def generateList4000(type_of_case: string):
    list = []
    if type_of_case == "best":
        for i in range(4000):
            list.append(i)
    elif type_of_case == "worst":
        for i in range(4000, 0, -1):
            list.append(i)
    elif type_of_case == "average":
        for i in range(4000):
            list.append(randint(0, 4000))
    return list

def generateList8000(type_of_case: string):
    list = []
    if type_of_case == "best":
        for i in range(8000):
            list.append(i)
    elif type_of_case == "worst":
        for i in range(8000, 0, -1):
            list.append(i)
    elif type_of_case == "average":
        for i in range(8000):
            list.append(randint(0, 8000))
    return list

def generateBestCase():
    #we will generate a list of 500, 1000, 2000, 4000, 8000 elements
    #we will time how long it takes to sort each list, once with bubble sort and once with gnome sort
    list500 = []
    list500.append(generateList500("best"))
    list1000 = []
    list1000.append(generateList1000("best"))
    list2000 = []
    list2000.append(generateList2000("best"))
    list4000 = []
    list4000.append(generateList4000("best"))
    list8000 = []
    list8000.append(generateList8000("best"))
    print("Bubble sort:")
    exec_time = timeit.timeit(lambda: bubbleSort(list500, 1), number=1)
    print("500 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list1000, 1), number=1)
    print("1000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list2000, 1), number=1)
    print("2000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list4000, 1), number=1)
    print("4000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list8000, 1), number=1)
    print("8000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    print("Gnome sort:")
    exec_time = timeit.timeit(lambda: gnomeSort(list500, 1), number=1)
    print("500 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(list1000, 1), number=1)
    print("1000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(list2000, 1), number=1)
    print("2000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(list4000, 1), number=1)
    print("4000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(list8000, 1), number=1)
    print("8000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")

def generateWorstCase():
    #we will generate a list of 500, 1000, 2000, 4000, 8000 elements
    #we will time how long it takes to sort each list, once with bubble sort and once with gnome sort
    #we will use the same list for both algorithms, so we will need a copy of the list
    list500 = []
    copy500 = []
    list500.append(generateList500("worst"))
    copy500.append(list500)
    list1000 = []
    copy1000 = []
    list1000.append(generateList1000("worst"))
    copy1000.append(list1000)
    list2000 = []
    copy2000 = []
    list2000.append(generateList2000("worst"))
    copy2000.append(list2000)
    list4000 = []
    copy4000 = []
    list4000.append(generateList4000("worst"))
    copy4000.append(list4000)
    list8000 = []
    copy8000 = []
    list8000.append(generateList8000("worst"))
    copy8000.append(list8000)
    print("Bubble sort:")
    #print the time with 4 decimals, in miliseconds
    exec_time = timeit.timeit(lambda: bubbleSort(list500, 1), number=1)
    print("500 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list1000, 1), number=1)
    print("1000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list2000, 1), number=1)
    print("2000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list4000, 1), number=1)
    print("4000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list8000, 1), number=1)
    print("8000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    print("Gnome sort:")
    exec_time = timeit.timeit(lambda: gnomeSort(copy500, 1), number=1)
    print("500 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(copy1000, 1), number=1)
    print("1000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(copy2000, 1), number=1)
    print("2000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(copy4000, 1), number=1)
    print("4000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(copy8000, 1), number=1)


def generateAverageCase():
    #we will generate a list of 500, 1000, 2000, 4000, 8000 elements
    #we will time how long it takes to sort each list, once with bubble sort and once with gnome sort
    #we will use the same list for both algorithms, so we will need a copy of the list
    list500 = []
    copy500 = []
    list500.append(generateList500("average"))
    copy500.append(list500)
    list1000 = []
    copy1000 = []
    list1000.append(generateList1000("average"))
    copy1000.append(list1000)
    list2000 = []
    copy2000 = []
    list2000.append(generateList2000("average"))
    copy2000.append(list2000)
    list4000 = []
    copy4000 = []
    list4000.append(generateList4000("average"))
    copy4000.append(list4000)
    list8000 = []
    copy8000 = []
    list8000.append(generateList8000("average"))
    copy8000.append(list8000)
    print("Bubble sort:")
    #print the time with 4 decimals, in miliseconds
    exec_time = timeit.timeit(lambda: bubbleSort(list500, 1), number=1)
    print("500 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list1000, 1), number=1)
    print("1000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list2000, 1), number=1)
    print("2000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list4000, 1), number=1)
    print("4000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: bubbleSort(list8000, 1), number=1)
    print("8000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    print("Gnome sort:")
    exec_time = timeit.timeit(lambda: gnomeSort(list500, 1), number=1)
    print("500 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(list1000, 1), number=1)
    print("1000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(list2000, 1), number=1)
    print("2000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(list4000, 1), number=1)
    print("4000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")
    exec_time = timeit.timeit(lambda: gnomeSort(list8000, 1), number=1)
    print("8000 elements: ", "{:.4f}".format(exec_time * 1000), "ms")



'''
Bubble sort algorithm complexity:
Best case: O(n) - when the list is already sorted, we pass through the list only once
Worst case: O(n^2) - when the list is sorted in reverse order, we pass through the list n times 
'''

def bubbleSort(list, step):
    n = len(list)
    s = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                s += 1
            #if s % step == 0:
                #print(list)
    #print(list)

'''
Gnome sort algorithm complexity:
Best case: O(n) - when the list is already sorted, we pass through the list only once
Worst case: O(n^2) - when the list is sorted in reverse order, we pass through the list n times
'''

"""
def gnomeSort(list, step):
    n = len(list)
    s = 0
    index = 0
    while index < n:
        if index == 0:
            index += 1
        if index < n and list[index] >= list[index-1]:
            index += 1
        else:
            list[index], list[index-1] = list[index-1], list[index]
            index -= 1
            s += 1
        if s % step == 0:
            print(list)
    print(list)
"""

def gnomeSort(my_list, step):
    n = len(my_list)
    s = 0
    index = 0
    while index < n:
        if index == 0:
            index += 1
        if index < n and my_list[index] < my_list[index - 1]:
            my_list[index], my_list[index - 1] = my_list[index - 1], my_list[index]
            index -= 1
            s += 1
        else:
            if index == 0:
                index += 1
            else:
                index += 1
        #if s % step == 0:
            #print(my_list)
    #print(my_list)

def main():
    list = []
    while True:
        print("1. Generate a list of n random natural numbers. Generated numbers must be between 0 and 100.")
        print("2. Sort the list using the first algorithm - bubble sort")
        print("3. Sort the list using the second algorithm - gnome sort")
        print("4. Best case")
        print("5. Worst case")
        print("6. Average case")
        print("0. Exit the program")
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
            generateBestCase()
        elif option == "5":
            generateWorstCase()
        elif option == "6":
            generateAverageCase()
        elif option == "0":
            break
        else:
            print("Invalid option!")

main()