# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import sqlalchemy as sc

# create connection to new and old database both of theme is mysql in one database two schema
engine = sc.create_engine('mysql+pymysql://root:root@localhost:3391/new_db')
engine2 = sc.create_engine('mysql+pymysql://root:root@localhost:3391/old_db')

# select map file from json file for each table




