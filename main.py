# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import os
import sqlalchemy as sc
from sqlalchemy import text
from dotenv import dotenv_values, load_dotenv
from utils import db

path = os.getcwd()
load_dotenv(os.path.join(path, '.env'))

# check for .env file if it's not available print error message and abort
if not os.path.isfile('.env'):
    print(".env file not found", )
    exit()

schemas_dir = os.path.join(path, 'schemas')
files = os.listdir(schemas_dir)
databased = files[0].split(".")[0]

db_engine = db.DB(path, databased)

base_tables = db_engine.base_db.execute(text("select all tables"))

print(base_tables)