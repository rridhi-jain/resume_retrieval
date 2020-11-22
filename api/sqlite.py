import sqlite3
import json

def create_table(conn):
  conn.execute('DROP TABLE resumes;')
  conn.execute('CREATE TABLE IF NOT EXISTS resumes (id integer PRIMARY KEY, resume_name text NOT NULL, url text NOT NULL, vector_model json, cluster text );')
  return True

def save_in_db(result, corpus_name):
  conn = sqlite3.connect('ResumeRetrieval.db')
  create_table(conn)
  values = []
  i = 1
  for value in result:
    values.append((i, corpus_name[i-1], "resumes/"+corpus_name[i-1], json.dumps(value)))
    i += 1
  print("Executing query")
  result = conn.executemany('INSERT INTO resumes (id, resume_name, url, vector_model) VALUES (?,?,?,?)', values)
  conn.commit()
  conn.close()
  return "Successfully inserted"


def get_all_records():
  conn = sqlite3.connect('ResumeRetrieval.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM resumes;')
  result = cursor.fetchall()
  return result