import sqlite3 as db

conn = db.connect("UR_Connect.db")

create_student_table_query = (f'''
     CREATE TABLE IF NOT EXISTS STUDENTS
     (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     student_id INTEGER NOT NULL UNIQUE,
     first_name VARCHAR(200) NOT NULL,
     last_name VARCHAR(200) NOT NULL,
     email VARCHAR(200) NOT NULL UNIQUE,
     password VARCHAR(50) NOT NULL,
     resume TEXT ,
     major TEXT ,
     looking_for_job BIT,
     bio TEXT ,
     Applied_jobs_id INTEGER,
     date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     date_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     FOREIGN KEY (Applied_jobs_id) REFERENCES JOBS(ID)
     );''')
conn.execute(create_student_table_query)


create_employer_table_query = (f'''
    CREATE TABLE IF NOT EXISTS EMPLOYERS
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    company_name VARCHAR(250),
    email VARCHAR(200) NOT NULL UNIQUE,
    name VARCHAR(200) NOT NULL,
    is_hiring BIT,
    address VARCHAR(200) NOT NULL,
    phone_number VARCHAR(200) NOT NULL,
    password VARCHAR(50) NOT NULL,
    jobs_id INTEGER,
    FOREIGN KEY (jobs_id) REFERENCES JOBS(ID) 
    );''')
conn.execute(create_employer_table_query)


create_jobs_table_query = (f'''
    CREATE TABLE IF NOT EXISTS JOBS
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(250),
    description TEXT,
    filled BIT,
    address VARCHAR(200) NOT NULL,
    emp_id INTEGER,
    applicants_id INTEGER,
    posted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deadline TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (emp_id) REFERENCES EMPLOYERS(ID),
    FOREIGN KEY (applicants_id) REFERENCES STUDENTS(ID)
    );''')

conn.execute(create_jobs_table_query)
