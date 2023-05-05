# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

global conn
global cur


def create_table(table_name, fields):
    sql = 'create table if not exists ' + table_name + '(' + fields + ')'
    cur.execute(sql)
    conn.commit()


def del_table(table_name):
    sql = 'drop table ' + table_name
    cur.execute(sql)
    conn.commit()


def remake(table_name):
    del_table(table_name)
    create_table(table_name)
    # insert_record(1)
    conn.commit()


def insert_record(table_name, fields, data):
    sql = 'insert into ' + table_name + ' (' + fields + ') values (?, ?, ?);'
    cur.execute(sql, data)
    print('Inserted record ', data)
    conn.commit()


def fill_table_students():
    create_table('Students', 'School_Id INT PRIMARY KEY, Student_Id INT, Student_Name TEXT')
    fields_students = 'School_Id, Student_Id, Student_Name'
    data_students = [[1, 201, "Иван"],
                     [2, 202, "Петр"],
                     [3, 203, "Анастасия"],
                     [4, 204, "Игорь"]]

    for d in range(len(dataStudents)):
        insert_record('Students', fieldsStudents, dataStudents[d])


def close_conn():
    cur.close()
    conn.close()


db = 'teachers.db'
conn = sqlite3.connect(db)
cur = conn.cursor()


get_student_id = (input('Введите Id студента: '))
query = """SELECT s.Student_Id,
                  s.Student_Name,
                  l.School_Id,
                  l.School_Name
           FROM Students s, School l
           WHERE Student_Id=? AND s.School_Id = l.School_Id"""

cur.execute(query, (get_student_id,))
student = cur.fetchall()

try:
    print("ID Студента: " + str(student[0][0]) + "\n" 
      "Имя студента: " + student[0][1] + "\n"
      "ID школы: " + str(student[0][2]) + "\n"
      "Название школы: " + student[0][3] + "\n")
except TypeError:
    print("Нет такого студента")

close_conn()


# del_table('Students')
# remake('Students')
# fill_table_students

