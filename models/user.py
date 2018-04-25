#import sqlite3
from db import db 

class UserModel(db.Model):# database classes
    __tablename__ = 'users' #telling SQLAlchemy table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, username, password):
        #self.id = _id
        self.username = username
        self.password = password
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def find_by_username(cls, username):
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()
#        select = "SELECT * FROM users where username = ?"
#        res = cursor.execute(select, (username,)) # , is required to indicate tuple
#        row =   res.fetchone()
#        if row:
#            #user = cls(row[0], row[1], row[1])
#            user = cls(*row)
#        else:
#            user = None
#        connection.close()
        return cls.query.filter_by(username=username).first()
        
    @classmethod       
    def find_by_id(cls, _id):
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()
#        select = "SELECT * FROM users where id = ?"
#        res = cursor.execute(select, (_id,)) # , is required to indicate tuple
#        row =   res.fetchone()
#        if row:
#            #user = cls(row[0], row[1], row[1])
#            user = cls(*row)
#        else:
#            user = None                    
#        connection.close()
        return cls.query.filter_by(id=_id).first()