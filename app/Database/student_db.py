import sqlite3 as db
import os


def std_register(data):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SQLPATH = os.path.join(BASE_DIR, 'UR_CONNECT.db')

    conn = db.connect(SQLPATH)
    conn.execute("INSERT INTO STUDENTS('first_name', 'last_name', 'email', 'student_id', 'password') \
                 VALUES(?, ?, ?, ?, ?)",
                 (data['first_name'], data['last_name'], data['email'], data['student_id'], data['password']))

    conn.commit()
    conn.close()