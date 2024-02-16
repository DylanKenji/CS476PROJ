import sqlite3


class DbOperation:

    # opens database
    def db_op(self):
        con = sqlite3.connect('UR_Connect.db')
        return con

    #creates table for new passwords
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
        std_first_name = data['std_first_name']
        std_first_name = data['std_first_name']
        std_last_name = data['std_last_name']
        std_email = data['std_email']
        password = data['password']
        std_major = data['std_major']
        con = self.db_op()
        query = f'''
               INSERT INTO {name}('user_id', 'std_first_name', 'std_last_name', 'std_email', 'password', 'std_major') 
               VALUES(?, ?, ?, ?, ?, ?);
               '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query, (user_id, std_first_name, std_last_name, std_email, password))

    # retrieves data from vault based on user ID of account
    def show_record(self, user_id, name="pass_vault"):
        con = self.db_op()
        query = f'''
               SELECT * FROM {name} WHERE user_id=?;
               '''
        with con as con:
            cursor = con.cursor()
            records_list = cursor.execute(query, (user_id,))
            return records_list

    # deletes account from password table based on user ID
    def delete_record(self, ID, name="pass_vault"):
        con = self.db_op()
        query = f'''
               DELETE FROM {name} WHERE ID =?;
               '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query, (ID,))

    # retrieves encrypted password from password vault from account based on user ID
    def get_account_password(self, ID, name="pass_vault"):
        con = self.db_op()
        query = f'''
               SELECT password FROM {name} WHERE ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (ID,)).fetchone()
            return result[0]

    # creates master table for master accounts, ie. new users
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
            password VARCHAR(50),
            FOREIGN KEY (emp_jobs_id) REFERENCES jobs_table(jobs_ID)
            );
        '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query)

    # inputs new account into Master table
    def create_master_record(self, data, name="master_table"):
        username = data['username']
        password = data['password']
        con = self.db_op()
        query = f'''
               INSERT INTO {name}('username', 'password') 
               VALUES(?, ?);
               '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query, (username, password))

    # deletes account from master table based on User ID
    def delete_master_record(self, ID, name="master_table"):
        con = self.db_op()
        query = f'''
               DELETE FROM {name} WHERE ID =?;
               '''
        with con as con:
            cursor = con.cursor()
            cursor.execute(query, (ID,))

    # retrieves master password hash based on username
    def get_stored_password(self, username, name="master_table"):
        con = self.db_op()
        query = f'''
               SELECT password FROM {name} WHERE username=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (username,)).fetchone()

            if result is not None:
                return result[0]
            else:
                return None

    # retrieves master password hash based on ID
    def get_master_password(self, ID, name="master_table"):
        con = self.db_op()
        query = f'''
               SELECT password FROM {name} WHERE ID=? ;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (ID,)).fetchone()

            return result[0]

    # retrieves user ID based on matching username and password
    def get_user_id(self, username, password, name="master_table"):
        con = self.db_op()
        query = f'''
               SELECT ID FROM {name} WHERE username=? AND password=?;
               '''
        with con as con:
            cursor = con.cursor()
            result = cursor.execute(query, (username, password)).fetchone()
            if result:
                return result[0]
            return None

    def create_jobs_table(self, name="jobs_table"):
        con = self.db_op()
        query = f'''
        CREATE TABLE IF NOT EXISTS {name}(
            jobs_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            job_name VARCHAR(250),
            job_description TEXT,
            emp_name VARCHAR(200) NOT NULL,
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
