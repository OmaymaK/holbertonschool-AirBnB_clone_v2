#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ amenity class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable = False)
    else:
        name = ""
    
    def __init__(self, *args, **kwargs):
        """Initialize Amenity."""
        super().__init__(*args, **kwargs)
