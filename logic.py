import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database # имя базы данных
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE projects (
                            project_id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            project_name TEXT NOT NULL,
                            description TEXT,
                            url TEXT,
                            status_id INTEGER,
                            FOREIGN KEY(status_id) REFERENCES status(status_id)
                        )''')    
        
        
            conn.commit()

    
         
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE project_skills (
                            skill_id INTEGER FRONT KEY,
                            project_id INTEGER FRONT KEY,
                             FOREIGN KEY(status_id) REFERENCES status(status_id)
                        )''')    
            
            
            conn.commit()

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE status (
                            status_id INTEGER PRIMARY KEY,
                            status_name TEXT,
                            FOREIGN KEY(status_id) REFERENCES status(status_id)
                        )''')  

            conn.commit()


    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute(''' CREATE TABLE skills (
                             skills_id INTEGER PRIMARY KEY,
                             skills_name TEXT,
                            FOREIGN KEY(status_id) REFERENCES status(status_id)
                        )''')      
        conn.commit()
        
        