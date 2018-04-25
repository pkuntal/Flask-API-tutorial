# -*- coding: utf-8 -*-

#import sqlite3
from db import db 

class StoreModel(db.Model):# database classes
    __tablename__ = 'stores' #telling SQLAlchemy table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
#A key feature to enable management of a large collection is the so-called “dynamic” relationship. 
#This is an optional form of relationship() which returns a Query object in place of a collection when accessed.
#filter() criterion may be applied as well as limits and offsets, either explicitly or via array slices:
    items = db.relationship('ItemModel', lazy='dynamic') #prevents to create

    def __init__(self, name):
        self.name = name
        
    def json(self):
        return {'name':self.name, 'items': [item.json() for item in self.items.all()]}        
        
    def save_to_db(self): #creating, udating
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()
#        query = "INSERT INTO items VALUES(?,?)"
#        cursor.execute(query, (self.name, self.price,))
#        connection.commit()
#        connection.close()
        db.session.add(self)
        db.session.commit()
          
    @classmethod    
    def find_by_name(cls, name):
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()
#        query = "SELECT *  FROM Items WHERE name=?"
#        res = cursor.execute(query, (name,))
#        row = res.fetchone()
#        connection.close()
#        if row:
#            #return cls(row[0], row[1])
#            return cls(*row)
        #USING SQL ALACHEMY
        return cls.query.filter_by(name=name).first() #only first row
        
#    def update(self):
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()
#        query = "UPDATE items SET price = ? WHERE name=?"
#        cursor.execute(query, (self.price, self.name,))
#        connection.commit()
#        connection.close()
#        #return {'message':'Item Updated'}, 203
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

