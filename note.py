# Notes and Todo Software
# main class file for note operation
# brupoon

import sqlite3
 
def execute_sql(sql_command):
        
    conn = sqlite3.connect("note.db")
    cursor = conn.cursor()
    cursor.execute(sql_command)
    conn.commit()
    conn.close()

def initalize_db():
     
    sql_ = """
        CREATE TABLE note (
        number INTEGER PRIMARY KEY,
        date INTEGER,
        text VARCHAR(255),
        done INTEGER);"""
    execute_sql(sql_)
   
class Note():

    def __init__(self, date, text):
        
        self.date = date
        self.text = text
        
        if self.date == -1:
            self.todo = True
            self.appt = False
        else:
            self.todo = False
            self.appt = True

    def store_note(self):
        
        sql_ = """
        INSERT into note (date, text, done) VALUES (NULL, "{0}", "{1}", 0);
        """.format(self.date, self.text)
        execute_sql(sql_)

    def get_all_notes(self):

        sql_ = """
        SELECT * FROM note WHERE done = 0"""
        execute_sql(sql_)

    def remove_note(self, number):
       #for next time
       pass
