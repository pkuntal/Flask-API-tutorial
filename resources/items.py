# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:53:41 2018

@author: pkuntal
"""
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item_model import ItemModel


#items = []

class Item(Resource): #Student inherited from Resource
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
        # filter returns filter object, next on filter object 
        # first item from filter object. using None in the end 
        # if next doesnt find anything, return None
       item = ItemModel.find_by_name(name)
       if item:
            return item.json(), 200
       return {'message':'Item not found'}, 404
            #item = next(filter(lambda i:i['name'] == name, items), None)
        #return {'item':item}, 200 if item else 404
       
    @jwt_required()
    def post(self, name):
        #data = request.get_json(force=True) #dont check header
        #data = request.get_json(silent=True) # return none if error in header        
        #data = request.get_json()
        if ItemModel.find_by_name(name):
            return {"message":"Item with this name '{}' already exists".format(name)}, 400
        data = Item.parser.parse_args()
        print("inut json is {}".format(data))
        #item = {'name' : name, 'price': data['price']}
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()     
        except:
            return {"message":"An error occured during insertion"}, 500
        return item.json(), 201
#        if next(filter(lambda i:i['name'] == name, items), None) is not None:
#            return {'message':"An item with name{} already exists".format(name)}, 400
#        data = Item.parser.parse_args()
#        item = {'name' : name, 'price': data['price']}
#        items.append(item)
#        return item, 201 #201 - Created

   
    
    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
#            connection = sqlite3.connect('data.db')
#            cursor = connection.cursor()
#            query = "DELETE FROM items WHERE name=?"
#            cursor.execute(query, (name,))
#            connection.commit()
#            connection.close()
            
            return {'message':'Item deleted'}, 203
        else:
            return {"message":"Item with this name'{}' doesnt exist".format(name)}, 400
#        global items
#        items = list(filter(lambda i:i['name'] != name, items))        
    
    @jwt_required()
    def put(self, name):
         data = Item.parser.parse_args()
         
         item = ItemModel.find_by_name(name)
         if item is None:
             item = ItemModel(name, data['price'], data['store_id'])
#             try:
#                 item.insert()
#             except:
#                 return {"message":"An error occured during insertion"}, 500
         else:
             item.price = data['price']
#             try:
#                 item.update()
#             except:
#                 return {"message":"An error occured during Update"}, 500
             
         item.save_to_db()
         return item.json(), 201
    
#        data = Item.parser.parse_args()
#        #print(data['another'])
#        item = {'name':name, 'price':data['price']}
#        if next(filter(lambda i:i['name'] == name, items), None) is None:           
#            items.append(item)
#        else:
#            item.update(data)
#        return item


class ItemList(Resource):
    @jwt_required()
    def get(self):
        
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()
#        query = "SELECT * FROM items"
#        items = []
#        for row in cursor.execute(query):
#            items.append({'name':row[0], 'price':row[1]})
#        connection.commit()
#        connection.close()
        #return {'items':list(map(lambda x:x.json(),ItemModel.query.all()))}
        return {'items':[item.json() for item in ItemModel.query.all()]}