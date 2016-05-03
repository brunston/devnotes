# testing the package
# brupoon

import note
import sqlite3
db = note.initialize_db()

dated = note.Note('20160530','appointment')
dated.store_note()
undated = note.Note('-1','todo')
undated.store_note()
conn = sqlite3.connect("note.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM note")

print("fetchall:")
for r in cursor.fetchall():
    print(r)
