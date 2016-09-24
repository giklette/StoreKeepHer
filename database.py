# -*- coding: utf-8 -*-

import sqlite3
from bottle import response, request
import uuid

class DataBase():
    """
    Provide an interface to the database for a 'storekeepher' web application
    """

    def __init__(self, dbname="storekeepher.db"):
        """
        Constructor, database name is an optional parameter
        the default 'storekeepher.db' is suitable for most cases.
        """
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname)
        ### ensure that results returned from queries are strings rather
        ### than unicode 
        self.conn.text_factory = str
        
    def cursor(self):
        """
        Return a cursor on the database
        """        
        return self.conn.cursor()
    
    def commit(self):
        """
        Commit pending changes
        """
        self.conn.commit()


    def create_table(self):
        """
        Create database table for the likes application
        given a database connection 'db'.
        Removes any existing data that might be in the 
        database.
        """
        cursor = self.cursor()
        cursor.execute("DROP TABLE IF EXISTS likes")
        cursor.execute("DROP TABLE IF EXISTS sessions")
        cursor.execute("""
        CREATE TABLE likes (
        thing text,
        key text
        )""")
        cursor.execute("""
        CREATE TABLE sessions (
            key text unique primary key 
        )
        """)

    # likes management
    def store_like(self, key, like):
        """
        Store a new like in the database
        """
        cursor = self.cursor()
        cursor.execute("INSERT INTO likes (thing, key) VALUES (?, ?)", (like, key))
        self.commit()

    def get_likes(self, key):
        """
        Return a list of likes from the database
        """
        cursor = self.cursor()
        cursor.execute("SELECT thing FROM likes WHERE key=?", (key,))
        result = []
        for row in cursor:
            result.append(row[0])
        return result

    # sessions management
    def new_session(self):
        """
        Make a new session key, store it in the db.
        Add a cookie to the response with the session key and 
        return the new session key
        """
        # use the uuid library to make the random key
        key = str(uuid.uuid4())
        cur = self.cursor()
        # store this new session key in the database with no likes in the value
        cur.execute("INSERT INTO sessions VALUES (?)", (key,))
        self.commit()

        response.set_cookie('SESSION', key)
        
        return key

    def get_session(self):
        """
        Get the current session key if any, if not, return None
        """
        key = request.get_cookie('SESSION')
        
        cur = self.cursor()
        cur.execute("SELECT key FROM sessions WHERE key=?", (key,))
        
        row = cur.fetchone()
        if not row:
            # no existing session so we create a new one
            key = self.new_session()
        
        return key