#!/usr/bin/python3
""" 
    Import modules and packages 
"""
from numpy import place
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
