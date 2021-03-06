#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""
from datetime import datetime
import inspect
import models
import os
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__
