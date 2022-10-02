import sqlite3

with sqlite3.connect(r"resources\results.db") as conn:
    cur = conn.cursor()

    TABLECREATE = """CREATE TABLE IF NOT EXISTS tg_student_info(
            id INTEGER NOT NULL PRIMARY KEY,
            user_id INTEGER NOT NULL UNIQUE,
            user_name TEXT,
            full_name TEXT,
            length INTEGER,
            state INTEGER DEFAULT 0 NOT NULL
    );
    CREATE TABLE IF NOT EXISTS results_ever(
                id INTEGER NOT NULL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                Course TEXT NOT NULL,
                Grade_one INTEGER DEFAULT 0 NOT NULL,
                Grade_two INTEGER DEFAULT 0 NOT NULL,
                Grade_three INTEGER DEFAULT 0 NOT NULL,
                Grade_four INTEGER DEFAULT 0 NOT NULL,
                Grade_five INTEGER DEFAULT 0 NOT NULL,
                Grade_six INTEGER DEFAULT 0 NOT NULL,
                Grade_seven INTEGER DEFAULT 0 NOT NULL,
                Grade_eight INTEGER DEFAULT 0 NOT NULL,
                Grade_nine TEXT DEFAULT gg NOT NULL,
                Grade_ten TEXT DEFAULT gg NOT NULL 
    );"""
    cur.executescript(TABLECREATE)

def all_user_id():
    try:
        conn = sqlite3.connect(r"resources\results.db")
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM tg_student_info")
        results = cur.fetchall()
        list = []
        for i in results:
            list.append(i)
        return list

    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def restart_one_users_Full_name(full_name):
    try:
        conn = sqlite3.connect(r"resources\results.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM tg_student_info WHERE full_name = ?", (full_name,))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def delete_results():
    try:
        conn = sqlite3.connect(r"resources\results.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM results_ever")
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def restart_db():
    try:
        conn = sqlite3.connect(r"resources\results.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM tg_student_info")
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def check_user_id(user_id, user_name):
    try:
        conn = sqlite3.connect(r"resources\results.db")
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM tg_student_info WHERE user_id = ?", (user_id,))
        if  cur.fetchone() is None:
            cur.execute("INSERT INTO tg_student_info(user_id, user_name) VALUES(?, ?)", (user_id, user_name))
            conn.commit()
            return False
        else:
            return True
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_full_name_in_first_table(full_name, user_id):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE tg_student_info SET full_name = ? WHERE user_id = ?", (full_name, user_id))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_length(length, user_id):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE tg_student_info SET length = ? WHERE user_id = ?", (length, user_id))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def get_length(user_id):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("SELECT length FROM tg_student_info WHERE user_id = ?", (user_id,))
        return cur.fetchone()[0]
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def minus_one_length_and_plus_state(user_id):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE tg_student_info SET length = length - 1 WHERE user_id = ?", (user_id,))
        cur.execute("UPDATE tg_student_info SET state = state + 1 WHERE user_id = ?", (user_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def get_state(user_id):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("SELECT state FROM tg_student_info WHERE user_id = ?", (user_id,))
        return cur.fetchone()[0]
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def get_full_name(user_id):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("SELECT full_name FROM tg_student_info WHERE user_id = ?", (user_id,))
        return cur.fetchone()[0]
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_user_and_course(user, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO results_ever(user_id, course) VALUES (?, ?)", (user, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_question_one(results, user_id, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE results_ever SET Grade_one = ? WHERE user_id = ? AND course = ?", (results, user_id, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_question_two(results, user_id, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE results_ever SET Grade_two = ? WHERE user_id = ? AND course = ?", (results, user_id, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_question_three(results, user_id, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE results_ever SET Grade_three = ? WHERE user_id = ? AND course = ?", (results, user_id, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_question_four(results, user_id, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE results_ever SET Grade_four = ? WHERE user_id = ? AND course = ?", (results, user_id, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_question_five(results, user_id, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE results_ever SET Grade_five = ? WHERE user_id = ? AND course = ?", (results, user_id, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_question_six(results, user_id, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE results_ever SET Grade_six = ? WHERE user_id = ? AND course = ?", (results, user_id, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_question_seven(results, user_id, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE results_ever SET Grade_seven = ? WHERE user_id = ? AND course = ?", (results, user_id, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_question_eight(results, user_id, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE results_ever SET Grade_eight = ? WHERE user_id = ? AND course = ?", (results, user_id, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_question_nine(results, user_id, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE results_ever SET Grade_nine = ? WHERE user_id = ? AND course = ?", (results, user_id, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()

def add_question_ten(results, user_id, course):
    try:
        conn = sqlite3.connect(r'resources\results.db')
        cur = conn.cursor()
        cur.execute("UPDATE results_ever SET Grade_ten = ? WHERE user_id = ? AND course = ?", (results, user_id, course))
        conn.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cur.close()
        conn.close()