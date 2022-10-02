import pandas as pd


def list_Student(): #list (student, discipline)
    df = pd.read_excel(r"resources\liststudent.xls", usecols="B,G,I")
    df = df.sort_values(["Student"], ascending=True)
    lst = []
    for i in range(len(df)):
        c = df.iloc[i]['Student']
        b = df.iloc[i]['Course']
        b = b.replace('\t', '')
        lst.append((c, b))
    return lst

def set_discipline(): #list discipline
    df = pd.read_excel(r"resources\liststudent.xls", usecols="B,G,I")
    df = df.sort_values(["Student"], ascending=True)
    my_set = set()
    for i in range(len(df)):
        a = df.iloc[i]['Course']
        a = a.replace('\t', '')
        my_set.add(a)
    discipline = list(my_set)
    discipline.sort()
    return discipline

def set_people():#list sorted student
    df = pd.read_excel(r"resources\liststudent.xls", usecols="B,G,I")
    df = df.sort_values(["Student"], ascending=True)
    my_set = set()
    for i in range(len(df)):
        a = df.iloc[i]['Student']
        my_set.add(a)
    allpeople = list(my_set)
    allpeople.sort()
    return allpeople


def binary_search(list, item): #fast search student in list
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return True
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False

def search_all_discipline_for_student(full_name): #get list in format (student,all your discipline ...),(student2, discipline)
    lst = list_Student()
    discipline = []
    discipline.append(full_name)
    for i in range(len(lst)):
        if full_name in lst[i][0]:
            discipline.append(lst[i][1])
    return discipline

def search_length(list, user): #get index and lenghth
    a = 0
    for i in range(len(list)):
        if list[i][0] == user:
            a += 1
    return a


