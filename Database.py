import sqlite3

from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

import bcrypt

engine = create_engine('')
def create_conn():
    conn = sqlite3.connect("data/Account.db") 
    return conn

def init_database():
    conn = create_conn()
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )    
    ''')

    conn.commit()
    conn.close()

def signup(username, password):
    conn = create_conn()
    c = conn.cursor()

    
