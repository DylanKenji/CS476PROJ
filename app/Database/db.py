import sqlite3


class DbOperation:

    # opens database
    def db_op(self):
        con = sqlite3.connect('UR_Connect.db')
        return con

    # creates table for new passwords
    def create_student_table(self, name="student_table"):
        con = self.db_op()
        query = f'''
        CREATE TABLE IF NOT EXISTS {name}(
            std_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            student_id INTEGER NOT NULL,
            std_first_name VARCHAR(200) NOT NULL,
            std_last_name VARCHAR(200) NOT NULL,
            std_email VARCHAR(200) NOT NULL,
            password VARCHAR(50) NOT NULL,
            std_resume TEXT ,
            std_major TEXT NOT NULL,
            std_looking_for_job BIT,
            std_bio TEXT ,
            date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (std_Applied_job_id) REFERENCES jobs_table(jobs_ID)
            );
        '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query)

    # adds new values to student table when creating new account
    def create_record(self, data, user_id, name="student_table"):
        student_id = data['student_id']
        std_first_name = data['std_first_name']
        std_last_name = data['std_last_name']
        std_email = data['std_email']
        password = data['password']
        con = self.db_op()
        query = f'''
               INSERT INTO {name}('student_id' ,'std_first_name', 'std_last_name', 'std_email', 'password', 'std_major') 
               VALUES(?, ?, ?, ?, ?, ?);
               '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query, (user_id, std_first_name, std_last_name, std_email, password))

    # retrieves user ID based on matching email and password
    def get_std_id(self, email, password, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT std_ID FROM {name} WHERE std_email=? AND password=?;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (email, password)).fetchone()
            if result:
                return result[0]
            return None

    # retrieves all data from vault based on user ID of account
    def show_record(self, std_id, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT * FROM {name} WHERE std_id=?;
               '''
        with con as con:
            cursor = con.cursor()
            records_list = cursor.execute(query, (std_id,))
            return records_list

    # deletes account from password table based on user ID
    def delete_record(self, std_ID, name="pass_vault"):
        con = self.db_op()
        query = f'''
               DELETE FROM {name} WHERE std_ID =?;
               '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query, (std_ID,))

    # retrieves student ID from student table
    def get_studentid(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT student_id FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # retrieves student first name from student table
    def get_std_first_name(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT std_first_name FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # retrieves student last name from student table
    def get_std_last_name(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT std_last_name FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # retrieves student email from student table
    def get_sdt_email(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT std_email FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # retrieves encrypted password from students using the email
    def get_std_password(self, std_email, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT password FROM {name} WHERE std_email=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_email,)).fetchone()
            return result[0]

    # retrieves student resume from student table
    def get_std_resume(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT std_resume FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # retrieves student major from student table
    def get_std_major(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT std_major FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # retrieves student bio from student table
    def get_std_bio(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT std_bio FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # retrieves student looking for job status from student table
    def get_std_looking_for_job(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT std_looking_for_job FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # retrieves student date created from student table
    def get_std_date_created(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT date_created FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # retrieves student date updated from student table
    def get_std_date_updated(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT date_updated FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # retrieves student applied job ID from student table
    def get_std_applied_job_id(self, std_ID, name="student_table"):
        con = self.db_op()
        query = f'''
               SELECT std_Applied_job_id FROM {name} WHERE std_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (std_ID,)).fetchone()
            return result[0]

    # creates employer table for employer accounts
    def create_employer_table(self, name="employer_table"):
        con = self.db_op()
        query = f'''
        CREATE TABLE IF NOT EXISTS {name}(
            emp_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            company_name VARCHAR(250),
            emp_email VARCHAR(200) NOT NULL,
            emp_name VARCHAR(200) NOT NULL,
            emp_is_hiring BIT,
            emp_address VARCHAR(200) NOT NULL,
            emp_phone_number VARCHAR(200) NOT NULL,
            emp_address VARCHAR(200) NOT NULL,
            password VARCHAR(50) NOT NULL,
            FOREIGN KEY (emp_jobs_id) REFERENCES jobs_table(jobs_ID)
            );
        '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query)

    # inputs new account into employer table
    def create_emp_record(self, data, name="employer_table"):
        company_name = data['company_name']
        emp_email = data['emp_email']
        emp_name = data['emp_name']
        emp_is_hiring = data['emp_is_hiring']
        emp_address = data['emp_address']
        emp_phone_number = data['emp_phone_number']
        password = data['password']
        con = self.db_op()
        query = f'''
               INSERT INTO {name}('company_name', 'emp_email', 'emp_name', 'emp_is_hiring', 'emp_address', 'emp_phone_number', 'password') 
               VALUES(?, ?, ?, ?, ?, ?, ?);
               '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query,
                           (company_name, emp_email, emp_name, emp_is_hiring, emp_address, emp_phone_number, password))

    # deletes account from employer table based on User ID
    def delete_emp_record(self, emp_ID, name="employer_table"):
        con = self.db_op()
        query = f'''
               DELETE FROM {name} WHERE emp_ID =?;
               '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query, (emp_ID,))

    # retrieves master password hash based on username
    def get_stored_password(self, emp_email, name="master_table"):
        con = self.db_op()
        query = f'''
               SELECT password FROM {name} WHERE emp_email=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_email,)).fetchone()

            if result is not None:
                return result[0]
            else:
                return None

    # retrieves user ID based on matching username and password
    def get_emp_id(self, emp_email, password, name="employer_table"):
        con = self.db_op()
        query = f'''
               SELECT emp_ID FROM {name} WHERE emp_email=? AND password=?;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_email, password)).fetchone()
            if result:
                return result[0]
            return None

    # retrieve employer company name from employer table
    def get_company_name(self, emp_ID, name="employer_table"):
        con = self.db_op()
        query = f'''
               SELECT company_name FROM {name} WHERE emp_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_ID,)).fetchone()
            return result[0]

    # retrieve employer email from employer table
    def get_emp_email(self, emp_ID, name="employer_table"):
        con = self.db_op()
        query = f'''
               SELECT emp_email FROM {name} WHERE emp_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_ID,)).fetchone()
            return result[0]

    # retrieve employer name from employer table
    def get_emp_name(self, emp_ID, name="employer_table"):
        con = self.db_op()
        query = f'''
               SELECT emp_name FROM {name} WHERE emp_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_ID,)).fetchone()
            return result[0]

    # retrieve employer is hiring status from employer table
    def get_emp_is_hiring(self, emp_ID, name="employer_table"):
        con = self.db_op()
        query = f'''
               SELECT emp_is_hiring FROM {name} WHERE emp_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_ID,)).fetchone()
            return result[0]

    # retrieve employer address from employer table
    def get_emp_address(self, emp_ID, name="employer_table"):
        con = self.db_op()
        query = f'''
               SELECT emp_address FROM {name} WHERE emp_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_ID,)).fetchone()
            return result[0]

    # retrieve employer phone number from employer table
    def get_emp_phone_number(self, emp_ID, name="employer_table"):
        con = self.db_op()
        query = f'''
               SELECT emp_phone_number FROM {name} WHERE emp_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_ID,)).fetchone()
            return result[0]

    # retrieve employer date created from employer table
    def get_emp_date_created(self, emp_ID, name="employer_table"):
        con = self.db_op()
        query = f'''
               SELECT date_created FROM {name} WHERE emp_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_ID,)).fetchone()
            return result[0]

    # retrieve employer date updated from employer table
    def get_emp_date_updated(self, emp_ID, name="employer_table"):
        con = self.db_op()
        query = f'''
               SELECT date_updated FROM {name} WHERE emp_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_ID,)).fetchone()
            return result[0]

    # retrieve employer job ID from employer table
    def get_emp_jobs_id(self, emp_ID, name="employer_table"):
        con = self.db_op()
        query = f'''
               SELECT emp_jobs_id FROM {name} WHERE emp_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (emp_ID,)).fetchone()
            return result[0]

    # creates jobs table for job postings
    def create_jobs_table(self, name="jobs_table"):
        con = self.db_op()
        query = f'''
        CREATE TABLE IF NOT EXISTS {name}(
            jobs_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            job_name VARCHAR(250),
            job_description TEXT,
            job_filled BIT,
            job_address VARCHAR(200) NOT NULL,
            job_posted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            job_deadline TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (emp_id) REFERENCES emp_table(emp_ID),
            FOREIGN KEY (job_applicants_id) REFERENCES student_table(std_ID)
            );
        '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query)

    # creates new job posting in jobs table
    def create_job_record(self, data, name="jobs_table"):
        job_name = data['job_name']
        job_description = data['job_description']
        job_filled = data['job_filled']
        job_address = data['job_address']
        job_deadline = data['job_deadline']
        con = self.db_op()
        query = f'''
               INSERT INTO {name}('job_name', 'job_description', 'job_filled', 'job_address', 'job_deadline') 
               VALUES(?, ?, ?, ?, ?);
               '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query, (job_name, job_description, job_filled, job_address, job_deadline))

    # deletes job posting from jobs table based on job ID
    def delete_job_record(self, jobs_ID, name="jobs_table"):
        con = self.db_op()
        query = f'''
               DELETE FROM {name} WHERE jobs_ID =?;
               '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query, (jobs_ID,))

    # retrieves job name from jobs table
    def get_job_name(self, jobs_ID, name="jobs_table"):
        con = self.db_op()
        query = f'''
               SELECT job_name FROM {name} WHERE jobs_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (jobs_ID,)).fetchone()
            return result[0]

    # retrieves job description from jobs table
    def get_job_description(self, jobs_ID, name="jobs_table"):
        con = self.db_op()
        query = f'''
               SELECT job_description FROM {name} WHERE jobs_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (jobs_ID,)).fetchone()
            return result[0]

    # retrieves job filled status from jobs table
    def get_job_filled(self, jobs_ID, name="jobs_table"):
        con = self.db_op()
        query = f'''
               SELECT job_filled FROM {name} WHERE jobs_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (jobs_ID,)).fetchone()
            return result[0]

    # retrieves job address from jobs table
    def get_job_address(self, jobs_ID, name="jobs_table"):
        con = self.db_op()
        query = f'''
               SELECT job_address FROM {name} WHERE jobs_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (jobs_ID,)).fetchone()
            return result[0]

    # retrieves job posted date from jobs table
    def get_job_posted_date(self, jobs_ID, name="jobs_table"):
        con = self.db_op()
        query = f'''
               SELECT job_posted_date FROM {name} WHERE jobs_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (jobs_ID,)).fetchone()
            return result[0]

    # retrieves job deadline from jobs table
    def get_job_deadline(self, jobs_ID, name="jobs_table"):
        con = self.db_op()
        query = f'''
               SELECT job_deadline FROM {name} WHERE jobs_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (jobs_ID,)).fetchone()
            return result[0]

    # retrieves employer ID from jobs table
    def get_emp_job_id(self, jobs_ID, name="jobs_table"):
        con = self.db_op()
        query = f'''
               SELECT emp_id FROM {name} WHERE jobs_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (jobs_ID,)).fetchone()
            return result[0]

    # retrieves job applicants ID from jobs table
    def get_job_applicants_id(self, jobs_ID, name="jobs_table"):
        con = self.db_op()
        query = f'''
               SELECT job_applicants_id FROM {name} WHERE jobs_ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (jobs_ID,)).fetchone()
            return result[0]