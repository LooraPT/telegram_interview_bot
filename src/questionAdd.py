from src.database import *

def questionAddOne(StudentAndDiscipline, user_id, query):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(user_id) == StudentAndDiscipline[i][0]:
            add_question_one(query, user_id, StudentAndDiscipline[i - 1 + get_state(user_id)][1])
            break

def questionAddTwo(StudentAndDiscipline, user_id, query):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(user_id) == StudentAndDiscipline[i][0]:
            add_question_two(query, user_id, StudentAndDiscipline[i - 1 + get_state(user_id)][1])
            break

def questionAddThree(StudentAndDiscipline, user_id, query):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(user_id) == StudentAndDiscipline[i][0]:
            add_question_three(query, user_id, StudentAndDiscipline[i - 1 + get_state(user_id)][1])
            break

def questionAddFour(StudentAndDiscipline, user_id, query):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(user_id) == StudentAndDiscipline[i][0]:
            add_question_four(query, user_id, StudentAndDiscipline[i - 1 + get_state(user_id)][1])
            break

def questionAddFive(StudentAndDiscipline, user_id, query):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(user_id) == StudentAndDiscipline[i][0]:
            add_question_five(query, user_id, StudentAndDiscipline[i - 1 + get_state(user_id)][1])
            break

def questionAddSix(StudentAndDiscipline, user_id, query):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(user_id) == StudentAndDiscipline[i][0]:
            add_question_six(query, user_id, StudentAndDiscipline[i - 1 + get_state(user_id)][1])
            break

def questionAddSeven(StudentAndDiscipline, user_id, query):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(user_id) == StudentAndDiscipline[i][0]:
            add_question_seven(query, user_id, StudentAndDiscipline[i - 1 + get_state(user_id)][1])
            break

def questionAddEight(StudentAndDiscipline, user_id, query):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(user_id) == StudentAndDiscipline[i][0]:
            add_question_eight(query, user_id, StudentAndDiscipline[i - 1 + get_state(user_id)][1])
            break

def questionAddNine(StudentAndDiscipline, user_id, query):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(user_id) == StudentAndDiscipline[i][0]:
            add_question_nine(query, user_id, StudentAndDiscipline[i - 1 + get_state(user_id)][1])
            break

def questionAddTen(StudentAndDiscipline, user_id, query):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(user_id) == StudentAndDiscipline[i][0]:
            add_question_ten(query, user_id, StudentAndDiscipline[i - 1 + get_state(user_id)][1])
            break

