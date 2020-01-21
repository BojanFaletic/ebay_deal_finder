import sqlite3
from sqlite3 import Error

DB_NAME = 'items.db'

def crete_connection(name):
  conn = None
  try:
    conn = sqlite3.connect(name)
  except Error as er:
    print(er)
  return conn


def delete_table(conn):
  sql = ''' delete from items '''
  cursor = conn.cursor()
  cursor.execute(sql)

def create_task(conn, task):
  sql = ''' INSERT INTO items(Name, Price, Actual_price)
            VALUES(?, ?, ?)'''
  cursor = conn.cursor()
  cursor.execute(sql, task)
  return cursor.lastrowid

def write_results(results):
  conn = crete_connection(DB_NAME)
  with conn:
    delete_table(conn)
    for itm in results:
      task_1 = (itm[0], itm[1], itm[2])
      create_task(conn, task_1)

