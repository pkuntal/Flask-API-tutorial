# -*- coding: utf-8 -*-

#import sqlite3
from db import db 

class ItemModel(db.Model):# database classes
    __tablename__ = 'items' #telling SQLAlchemy table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    
    store = db.relationship('StoreModel')



    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
        
    def json(self):
        return {'name':self.name, 'price':self.price}
        
        
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

