#!/usr/bin/python3
"""
Defines a class 'User'
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The class 'User' that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
