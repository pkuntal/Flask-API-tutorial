# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 09:53:26 2018

@author: pkuntal
"""
#from security import authenticate, identity
from resources.user import UserRegister
from resources.items import Item, ItemList
from flask_restful import Api
from flask_jwt import JWT
from flask import Flask, jsonify
from security import authenticate, identity as identity_function 
from datetime import timedelta
from resources.store import Store, StoreList
 

app = Flask(__name__)
api = Api(app)
app.secret_key = 'Pooja'


#Change the authentication endpoint (by default, /auth);
app.config['JWT_AUTH_URL_RULE'] = '/login' # now its login
#Change the token expiration time (by default, 5 minutes); changing it to 30mins
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
#Change the authentication key name (by default, username)
#app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
# putting Flask Modification tracker off because SQL Alchemy will use its own tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

@app.before_first_request
def create_tables():
    db.create_all()

#customizing JWT auth response
#this will return only access_code
#jwt = JWT(app, authenticate, identity) #/auth will call jwt
jwt = JWT(app, authenticate, identity_function)
@jwt.auth_response_handler
def customized_res_handler(access_token, identity):
    return jsonify({'acccess_token':access_token.decode('utf-8'), 
                    'user_id':identity.id})# UserModel object which contains a field id.
@jwt.jwt_error_handler
def customized_err_handler(error):
    return jsonify({'error_message':error.description,
                    'error_code':error.status_code}), error.status_code

api.add_resource(Item, '/item/<string:name>') # accessing http://127.0.0.1:3999/student/Pooja
api.add_resource(ItemList, '/items')

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister,'/register')


if __name__ == '__main__': #to exclude it from import if smeone import this file, these ines shouldnt be imported.
    from db import db
    db.init_app(app) # avoid circular import
    app.run(port=3999)

#defining end-point
#@app.route('/psmicroservice/v1/api/DASHProvisioning/<string:command>', methods=['POST', 'GET'])
#def handleRequests(command):
#    return command

#app.run(port=6502)



