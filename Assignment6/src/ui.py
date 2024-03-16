#
# This is the program's UI module. The user interface and all interaction with the user
# (print and input statements) are found here


# TODO for A6: problem 2

import functions
from copy import deepcopy


def test_all():
    '''
    Tests all functions
    '''
    functions.test_add_contestant()
    functions.test_insert_contestant()
    functions.test_remove_contestant()
    functions.test_remove_start_to_end()
    functions.test_replace_score()
    print("All tests passed!")


'''

(C) Display participants whose score has different properties.
list
list sorted
list [ < | = | > ] <score>
e.g.
list – display participants and all their scores
list < 4 – display participants with an average score <4
list = 6 – display participants with an average score =6
list sorted – display participants sorted in decreasing order of average score

'''

def list_contestant(contestants_list: list, contestant: int):
    '''
    Displays the given contestant and their scores
    '''
    print(f'Contestant {contestant} with scores: {functions.get_p1(contestants_list, contestant)}, '
          f'{functions.get_p2(contestants_list, contestant)}, {functions.get_p3(contestants_list, contestant)}')

def list(contestants_list: list):
    '''
    Displays all contestants and their scores
    '''
    for i in range(len(contestants_list)):
        list_contestant(contestants_list, i)

def list_with_average(contestants_list: list):
    '''
    Displays all contestants and their scores, along with their average score
    '''
    for i in range(len(contestants_list)):
        print(f'Contestant {i} with scores: {functions.get_p1(contestants_list, i)}, '
              f'{functions.get_p2(contestants_list, i)}, {functions.get_p3(contestants_list, i)}'
              f' and an average score of {functions.average_score(contestants_list, i)}')

def list_sorted(contestants_list: list):
    '''
    Displays all contestants and their scores, sorted in descending order of average score
    '''
    for i in range(len(contestants_list) - 1):
        for j in range(i + 1, len(contestants_list)):
            if functions.average_score(contestants_list, i) < functions.average_score(contestants_list, j):
                contestants_list[i], contestants_list[j] = contestants_list[j], contestants_list[i]
    list_with_average(contestants_list)


def list_less(contestants_list: list, score: int):
    '''
    Displays all contestants with an average score less than the given score
    '''
    for i in range(len(contestants_list)):
        if functions.average_score(contestants_list, i) < score:
            list_contestant(contestants_list, i)

def list_equal(contestants_list: list, score: int):
    '''
    Displays all contestants with an average score equal to the given score
    '''
    for i in range(len(contestants_list)):
        if functions.average_score(contestants_list, i) == score:
            list_contestant(contestants_list, i)

def list_greater(contestants_list: list, score: int):
    '''
    Displays all contestants with an average score greater than the given score
    '''
    for i in range(len(contestants_list)):
        if functions.average_score(contestants_list, i) > score:
            list_contestant(contestants_list, i)

def list_score(contestants_list: list, sign: str, score: int):
    '''
    Displays all contestants with an average score that has the given sign compared to the given score
    '''
    if sign == '<':
        list_less(contestants_list, score)
    elif sign == '=':
        list_equal(contestants_list, score)
    elif sign == '>':
        list_greater(contestants_list, score)

'''

(D) Establish the podium
top <number>
top <number> <P1 | P2 | P3>
remove [ < | = | > ] <score>
e.g.
top 3 – display the 3 participants having the highest average score, in descending order of average score
top 4 P3 – display the 4 participants who obtained the highest score for P3, sorted descending by that score
remove < 70 – set the scores of participants having an average score <70 to 0
remove > 89 – set the scores of participants having an average score >89 to 0

'''

def top(contestants_list: list, number: int):
    '''
    Displays the given number of contestants with the highest average score, in descending order of average score
    '''
    for i in range(len(contestants_list) - 1):
        for j in range(i + 1, len(contestants_list)):
            if functions.average_score(contestants_list, i) < functions.average_score(contestants_list, j):
                contestants_list[i], contestants_list[j] = contestants_list[j], contestants_list[i]
    top = []
    for i in range(number):
        top.append(contestants_list[i])

    list_with_average(top)

def top_p1(contestants_list: list, number: int):
    '''
    Displays the given number of contestants with the highest score for problem 1, sorted descending by that score
    '''
    for i in range(len(contestants_list) - 1):
        for j in range(i + 1, len(contestants_list)):
            if functions.get_p1(contestants_list, i) < functions.get_p1(contestants_list, j):
                contestants_list[i], contestants_list[j] = contestants_list[j], contestants_list[i]
    top = []
    for i in range(number):
        top.append(contestants_list[i])

    for i in range(len(top)):
        print(f'Contestant {i} with score P1: {functions.get_p1(top, i)}')

def top_p2(contestants_list: list, number: int):
    '''
    Displays the given number of contestants with the highest score for problem 2, sorted descending by that score
    '''
    for i in range(len(contestants_list) - 1):
        for j in range(i + 1, len(contestants_list)):
            if functions.get_p2(contestants_list, i) < functions.get_p2(contestants_list, j):
                contestants_list[i], contestants_list[j] = contestants_list[j], contestants_list[i]
    top = []
    for i in range(number):
        top.append(contestants_list[i])

    for i in range(len(top)):
        print(f'Contestant {i} with score P2: {functions.get_p2(top, i)}')

def top_p3(contestants_list: list, number: int):
    '''
    Displays the given number of contestants with the highest score for problem 3, sorted descending by that score
    '''
    for i in range(len(contestants_list) - 1):
        for j in range(i + 1, len(contestants_list)):
            if functions.get_p3(contestants_list, i) < functions.get_p3(contestants_list, j):
                contestants_list[i], contestants_list[j] = contestants_list[j], contestants_list[i]
    top = []
    for i in range(number):
        top.append(contestants_list[i])

    for i in range(len(top)):
        print(f'Contestant {i} with score P3: {functions.get_p3(top, i)}')


def top_p(contestants_list: list, number: int, problem):
    '''
    Displays the given number of contestants with the highest score for the given problem, sorted descending by that score
    '''
    if problem == 'P1':
        top_p1(contestants_list, number)
    elif problem == 'P2':
        top_p2(contestants_list, number)
    elif problem == 'P3':
        top_p3(contestants_list, number)


def save_state(contestants_list: list, undo_list: list):
    '''
    Saves the current state of the contestants list
    '''
    undo_list.append(deepcopy(contestants_list))





def print_menu():
    print("""
            User commands:
            add <P1 score> <P2 score> <P3 score>
            insert <P1 score> <P2 score> <P3 score> at <position>
            remove <position>
            remove <start position> to <end position>
            replace <position> <P1 | P2 | P3> with <new score>
            list
            list sorted
            list [ < | = | > ] <score>
            top <number>
            top <number> <P1 | P2 | P3>
            remove [ < | = | > ] <score>
            undo
            exit
            """)

def process_user_input(user_input):
    user_input = user_input.strip()
    commands = user_input.split(" ")
    command = commands[0]

    if len(commands) == 1:
        return command, ""

    return command, commands[1:]

def start_up():

    contestants_list = functions.generate_contestants_list()
    undo_list = []
    save_state(contestants_list, undo_list)

    while True:
        contestants_list = deepcopy(undo_list[-1])

        print_menu()
        user_input = input("Enter command: ")
        command, arguments = process_user_input(user_input)

        if command == "add":
            if len(arguments) != 3:
                print("Invalid number of arguments!")
                continue
            try:
                P1 = int(arguments[0])
                P2 = int(arguments[1])
                P3 = int(arguments[2])
                if (functions.check_score(P1) and functions.check_score(P2) and functions.check_score(P3)):
                    functions.add_contestant(contestants_list, P1, P2, P3)
                    save_state(contestants_list, undo_list)
                else:
                    raise ValueError
            except ValueError:
                print("Invalid score!")
                continue

        elif command == "insert":
            if len(arguments) != 5 or arguments[3] != "at":
                print("Invalid number of arguments!")
                continue
            try:
                P1 = int(arguments[0])
                P2 = int(arguments[1])
                P3 = int(arguments[2])
                position = int(arguments[4])
                if (functions.check_score(P1) and functions.check_score(P2) and functions.check_score(P3)
                        and functions.check_position(position, contestants_list)):
                    functions.insert_contestant(contestants_list, P1, P2, P3, position)
                    save_state(contestants_list, undo_list)
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input!")
                continue

        elif command == "remove":
            if len(arguments) == 1:
                try:
                    position = int(arguments[0])
                    if (functions.check_position(position, contestants_list)):
                        functions.remove_contestant(contestants_list, position)
                        save_state(contestants_list, undo_list)
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid position!")
                    continue

            elif len(arguments) == 3 and arguments[1] == "to":
                try:
                    start = int(arguments[0])
                    end = int(arguments[2])
                    if (functions.check_position(start, contestants_list) and functions.check_position(end, contestants_list)):
                        functions.remove_start_to_end(contestants_list, start, end)
                        save_state(contestants_list, undo_list)
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid positions!")
                    continue

            elif len(arguments) == 2 and arguments[0] in ["<", "=", ">"]:
                try:
                    score = int(arguments[1])
                    if functions.check_score(score):
                        functions.remove_score_with_sign(contestants_list, arguments[0], score)
                        save_state(contestants_list, undo_list)
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid score!")
                    continue

            else:
                print("Invalid number of arguments!")
                continue

        elif command == "replace":
            if len(arguments) != 4 or arguments[2] != "with":
                print("Invalid arguments!")
                continue
            try:
                position = int(arguments[0])
                P = arguments[1]
                score = int(arguments[3])
                if (functions.check_position(position, contestants_list) and functions.check_score(score)):
                    if P == "P1":
                        functions.replace_score(contestants_list, position, P, score)
                        save_state(contestants_list, undo_list)
                    elif P == "P2":
                        functions.replace_score(contestants_list, position, P, score)
                        save_state(contestants_list, undo_list)
                    elif P == "P3":
                        functions.replace_score(contestants_list, position, P, score)
                        save_state(contestants_list, undo_list)
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print("Invalid arguments!")
                continue

        elif command == "list":
            if len(arguments) == 0:
                list(contestants_list)

            elif len(arguments) == 1 and arguments[0] == "sorted":
                list_sorted(contestants_list)

            elif len(arguments) == 2 and arguments[0] in ["<", "=", ">"]:
                try:
                    score = int(arguments[1])
                    if functions.check_score(score):
                       list_score(contestants_list, arguments[0], score)
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid score!")
                    continue
            else:
                print("Invalid arguments!")
                continue

        elif command == "top":
            if len(arguments) == 1:
                try:
                    number = int(arguments[0])
                    if functions.check_position(number, contestants_list):
                        top(contestants_list, number)
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid number!")
                    continue

            elif len(arguments) == 2 and arguments[1] in ["P1", "P2", "P3"]:
                try:
                    number = int(arguments[0])
                    if functions.check_position(number, contestants_list):
                        top_p(contestants_list, number, arguments[1])
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid number!")
                    continue
            else:
                print("Invalid arguments!")
                continue

        elif command == "undo":
            if len(arguments) == 0:
                if len(undo_list) == 1:
                    print("No more undos!")
                    continue
                else:
                    functions.undo(undo_list)
            else:
                print("Invalid arguments!")
                continue

        elif command == "exit":
            break



