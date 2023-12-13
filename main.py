# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import os
import sqlalchemy as sc
from sqlalchemy import text
from dotenv import dotenv_values, load_dotenv

path = os.getcwd()

# check for .env file if it's not available print error message and abort
if not os.path.isfile('.env'):
    print(".env file not found", )
    exit()

load_dotenv(os.path.join(path, '.env'))

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

DB_CONNECTION_STRING = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/"


# define method that get array of two database names and connect to them
def connect_to_databases(databases):
    db_names = databases.split("-")
    new_database = sc.create_engine(DB_CONNECTION_STRING + db_names[0])
    old_database = sc.create_engine(DB_CONNECTION_STRING + db_names[1])
    return new_database, old_database


# set current path as default path
schemas_dir = os.path.join(path, 'schemas')

# get list of files in schemas directory
files = os.listdir(schemas_dir)
# get name of databases by split file name with "-"

base_db, target_db = None, None

for file in files:
    databases = file.split(".")[0]
    base_db, target_db = connect_to_databases(databases)

if base_db is not None and target_db is not None:
    print("connected to databases")
    base_db_tables = base_db.connect().execute(text("show tables"))
    for table in base_db_tables:
        print(table)

    target_db_tables = target_db.connect().execute(text("show tables"))
    for table in target_db_tables:
        print(table)

# create connection to new and old database both of theme is mysql in one database two schema
# new_database = sc.create_engine('mysql+pymysql://root:wp_root_password@localhost:3391/laravel')
# old_database = sc.create_engine('mysql+pymysql://root:wp_root_password@localhost:3391/old_crm')
#
# connection = new_database.connect()
#
# # Sample query
# results = connection.execute(text("SELECT * FROM brands where 1"))
# for row in results:
#     print(row)
#
