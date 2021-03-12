#!/usr/bin/python3
"""
Contains the TestPlaceDocs classes
"""

from datetime import datetime
import inspect
from models import place
from models.base_model import BaseModel
import os
import pep8
import unittest
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.attributes import InstrumentedAttribute
Place = place.Place
