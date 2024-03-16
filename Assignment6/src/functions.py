#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#

import random

'''
2. Contest
During a programming contest, each contestant had to solve 3 problems (named P1, P2 and P3). Afterwards,
an evaluation committee graded the solutions to each of the problems using integers between 0 and 10.
The committee needs a program that will allow managing the list of scores and establishing the winners.
Write a program that implements the functionalities exemplified below:

(A) Add the result of a new participant
add <P1 score> <P2 score> <P3 score>
insert <P1 score> <P2 score> <P3 score> at <position>
e.g.
add 3 8 10 – add a new participant with scores 3,8 and 10 (scores for P1, P2, P3 respectively)
insert 10 10 9 at 5 – insert scores 10, 10 and 9 at position 5 in the list (positions numbered from 0)

'''

def test_add_contestant():
    '''
    Tests add_contestant
    '''
    contestants_list = []
    add_contestant(contestants_list, 3, 8, 10)
    assert contestants_list == [[3, 8, 10]]
    add_contestant(contestants_list, 10, 10, 9)
    assert contestants_list == [[3, 8, 10], [10, 10, 9]]

def test_insert_contestant():
    '''
    Tests insert_contestant
    '''
    contestants_list = []
    insert_contestant(contestants_list, 3, 8, 10, 0)
    assert contestants_list == [[3, 8, 10]]
    insert_contestant(contestants_list, 10, 10, 9, 0)
    assert contestants_list == [[10, 10, 9], [3, 8, 10]]
    insert_contestant(contestants_list, 1, 2, 3, 1)
    assert contestants_list == [[10, 10, 9], [1, 2, 3], [3, 8, 10]]


def generate_contestant_scores():
    '''
    Generates a list of 3 random scores between 0 and 10
    '''
    P1 = random.randint(0, 10)
    P2 = random.randint(0, 10)
    P3 = random.randint(0, 10)
    return [P1, P2, P3]


def generate_contestants_list():
    '''
    Generates a list of 10 contestants, each with 3 random scores between 0 and 10
    '''
    contestants_list = []
    for i in range(10):
        contestants_list.append(generate_contestant_scores())
    return contestants_list


def add_contestant(contestants_list: list, P1, P2, P3):
    '''
    Adds a contestant with the given scores to the list
    :param contestants_list: the list of contestants
    :param P1: score for problem 1
    :param P2: score for problem 2
    :param P3: score for problem 3
    :return: -
    '''
    contestants_list.append([P1, P2, P3])


def insert_contestant(contestants_list: list, P1, P2, P3, position: int):
    '''
    Inserts a contestant with the given scores at the given position in the list
    :param contestants_list: the list of contestants
    :param P1: score for problem 1
    :param P2: score for problem 2
    :param P3: score for problem 3
    :param position: the position at which the contestant will be inserted
    :return: -
    '''
    contestants_list.insert(position, [P1, P2, P3])

'''

(B) Modify scores
remove <position>
remove <start position> to <end position>
replace <position> <P1 | P2 | P3> with <new score>
e.g.
remove 1 – set the scores of the participant at position 1 to 0
remove 1 to 3 – set the scores of participants at positions 1, 2 and 3 to 0
replace 4 P2 with 5 – replace the score obtained by participant 4 at P2 with 5

'''

def test_remove_contestant():
    '''
    Tests remove_contestant
    '''
    contestants_list = [[3, 8, 10], [10, 10, 9]]
    remove_contestant(contestants_list, 0)
    assert contestants_list == [[0, 0, 0], [10, 10, 9]]
    remove_contestant(contestants_list, 1)
    assert contestants_list == [[0, 0, 0], [0, 0, 0]]

def test_remove_start_to_end():
    '''
    Tests remove_start_to_end
    '''
    contestants_list = [[3, 8, 10], [10, 10, 9], [1, 2, 3], [3, 8, 10]]
    remove_start_to_end(contestants_list, 1, 2)
    assert contestants_list == [[3, 8, 10], [0, 0, 0], [0, 0, 0], [3, 8, 10]]

def test_replace_score():
    '''
    Tests replace_score
    '''
    contestants_list = [[3, 8, 10], [10, 10, 9], [1, 2, 3], [3, 8, 10]]
    replace_score(contestants_list, 1, 'P2', 5)
    assert contestants_list == [[3, 8, 10], [10, 5, 9], [1, 2, 3], [3, 8, 10]]
    replace_score(contestants_list, 0, 'P1', 5)
    assert contestants_list == [[5, 8, 10], [10, 5, 9], [1, 2, 3], [3, 8, 10]]
    replace_score(contestants_list, 3, 'P3', 5)
    assert contestants_list == [[5, 8, 10], [10, 5, 9], [1, 2, 3], [3, 8, 5]]


def remove_score(contestants_list: list, position: int, P1: int, P2: int, P3: int):
    '''
    Sets the scores of the contestant at the given position to the given scores
    '''
    set_p1(contestants_list, position, P1)
    set_p2(contestants_list, position, P2)
    set_p3(contestants_list, position, P3)

def set_p1(contestants_list: list, position: int, P1: int):
    '''
    Sets the score of the contestant at the given position for problem 1 to the given score
    '''
    contestants_list[position][0] = P1

def set_p2(contestants_list: list, position: int, P2: int):
    '''
    Sets the score of the contestant at the given position for problem 2 to the given score
    '''
    contestants_list[position][1] = P2

def set_p3(contestants_list: list, position: int, P3: int):
    '''
    Sets the score of the contestant at the given position for problem 3 to the given score
    '''
    contestants_list[position][2] = P3

def remove_contestant(contestants_list: list, position: int):
    '''
    Removes the scores of the contestant at the given position from the list(sets them to 0)
    :param contestants_list: list of contestants
    :param position: the contestants to be removed
    :return: -
    '''
    remove_score(contestants_list, position, 0, 0, 0)


def remove_start_to_end(contestants_list: list, start: int, end: int):
    '''
    Removes the contestants between the given positions from the list
    :param contestants_list: list of contestants
    :param start: the starting position
    :param end: the ending position
    :return:
    '''
    for i in range(start, end + 1):
        remove_contestant(contestants_list, i)

def replace_score(contestants_list: list, contestant: int, problem, new_score: int):
    '''
    Replaces the score of the given contestant at the given problem with the given new score
    :param contestants_list: the contestants list
    :param contestant: the contestant's position
    :param problem: the problem which will be changed
    :param new_score: the replacement score
    :return:
    '''
    if problem == 'P1':
        set_p1(contestants_list, contestant, new_score)
    elif problem == 'P2':
        set_p2(contestants_list, contestant, new_score)
    elif problem == 'P3':
        set_p3(contestants_list, contestant, new_score)

def get_p1(contestants_list: list, contestant: int):
    '''
    Returns the score of the given contestant for problem 1
    '''
    return contestants_list[contestant][0]

def get_p2(contestants_list: list, contestant: int):
    '''
    Returns the score of the given contestant for problem 2
    '''
    return contestants_list[contestant][1]

def get_p3(contestants_list: list, contestant: int):
    '''
    Returns the score of the given contestant for problem 3
    '''
    return contestants_list[contestant][2]

def average_score(contestants_list: list, contestant: int):
    '''
    Returns the average score of the given contestant
    '''
    p1 = get_p1(contestants_list, contestant)
    p2 = get_p2(contestants_list, contestant)
    p3 = get_p3(contestants_list, contestant)
    sum = p1 + p2 + p3
    return sum / 3

def check_score(score):
    '''
    Checks if the given score is valid
    '''
    return score >= 0 and score <= 10

def check_position(position, contestants_list):
    '''
    Checks if the given position is valid
    '''
    return position >= 0 and position < len(contestants_list)


def remove_less(contestants_list: list, score: int):
    '''
    Sets the scores of contestants with an average score less than the given score to 0
    '''
    for i in range(len(contestants_list)):
        if average_score(contestants_list, i) < score:
            remove_contestant(contestants_list, i)

def remove_equal(contestants_list: list, score: int):
    '''
    Sets the scores of contestants with an average score equal to the given score to 0
    '''
    for i in range(len(contestants_list)):
        if average_score(contestants_list, i) == score:
            remove_contestant(contestants_list, i)

def remove_greater(contestants_list: list, score: int):
    '''
    Sets the scores of contestants with an average score greater than the given score to 0
    '''
    for i in range(len(contestants_list)):
        if average_score(contestants_list, i) > score:
            remove_contestant(contestants_list, i)

def remove_score_with_sign(contestants_list: list, sign: str, score: int):
    '''
    Sets the scores of contestants with an average score that has the given sign compared to the given score to 0
    '''
    if sign == '<':
        remove_less(contestants_list, score)
    elif sign == '=':
        remove_equal(contestants_list, score)
    elif sign == '>':
        remove_greater(contestants_list, score)

'''

(E) Undo
undo – the last operation that modified program data is reversed. The user can undo all operations 
performed since program start by repeatedly calling this function.

'''

def undo(undo_list: list):
    '''
    Reverses the last operation that modified program data
    '''
    if len(undo_list) > 0:
        undo_list.pop()
