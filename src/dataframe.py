import pandas as pd
import xlrd

class StudentXls:
    def __init__(self, name):
        self.workbook = xlrd.open_workbook(name, ignore_workbook_corruption=True)
        self.df = pd.read_excel(self.workbook, usecols="B,G,I")
        self.df = self.df.sort_values(["Student"], ascending=True)
    def list_Student(self): #list (student, discipline)
        lst = []
        for i in range(len(self.df)):
            c = self.df.iloc[i]['Student']
            b = self.df.iloc[i]['Course']
            #b = b.replace('\t', '') # if file have 'tab'
            lst.append((c, b))
        return lst

    def set_discipline(self): #list discipline
        my_set = set()
        for i in range(len(self.df)):
            a = self.df.iloc[i]['Course']
            a = a.replace('\t', '')
            my_set.add(a)
        discipline = list(my_set)
        discipline.sort()
        return discipline

    def set_people(self):       #list student
        my_set = set()
        for i in range(len(self.df)):
            a = self.df.iloc[i]['Student']
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

    def search_length(list, user): #get how many discipline have one student
        count = 0
        for i in range(len(list)):
            if list[i][0] == user:
                count += 1
        return count


