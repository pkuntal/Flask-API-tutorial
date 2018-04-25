# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:42:48 2018

@author: pkuntal
"""

from app import app
from db import db
db.init(app)

@app.before_first_request
def create_tables():
    db.create_all()
