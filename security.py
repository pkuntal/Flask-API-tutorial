# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:36:41 2018

@author: pkuntal
"""

from models.user import UserModel
from werkzeug.security import safe_str_cmp


#users = [   
#  {
#    "username":"pooja",
#    "password":"amd@123"
#  }
#]
#
#username_mapping = {"pooja" : {
#    "id":1,
#    "username":"pooja",
#    "password":"amd@123"
#}}
#
#userid_mapping = {1 : {
#    "id":1,
#    "username":"pooja",
#    "password":"amd@123"
#}}

#users = [   User(1, "Pooja", "amd@123")
#        ]
#username_mapping = {u.username: u for u in users}
#userid_mapping = {u.id: u for u in users}

def authenticate(uname, pwd):
    print("authenticate {}".format(uname))

    user = UserModel.find_by_username(uname) #returns None if nothing found
    if user is not None and safe_str_cmp(user.password, pwd):
        return user
    
def identity(payload):#JWT payload
    print("payload {}".format(payload))
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
    




