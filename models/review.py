#!/usr/bin/python3
""" 
    Import modules and packages 
"""

from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
