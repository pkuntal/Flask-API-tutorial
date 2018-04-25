# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:53:41 2018

@author: pkuntal
"""
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


#items = []

class Store(Resource): #Student inherited from Resource
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
                            type=float,
                            required=True, 
                            help="This field cant be left blank!")
    parser.add_argument('store_id', 
                            type=int,
                            required=True, 
                            help="Every items needs a store_id!")
    @jwt_required() #authenticate before GET, POST call
    def get(self, name): # GET method
       store = StoreModel.find_by_name(name)
       if store:
            return store.json(), 200
       return {'message':'Item not found'}, 404
   
    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message":"Item with this name '{}' already exists".format(name)}, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()     
        except:
            return {"message":"An error occured during insertion"}, 500
        
        return store.json(), 201
   
    
    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
#                   
            return {'message':'Item deleted'}, 203
        else:
            return {"message":"Item with this name'{}' doesnt exist".format(name)}, 400
#        global items
#        items = list(filter(lambda i:i['name'] != name, items))        
    
    
    
class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {'items':[store.json() for store in StoreModel.query.all()]}