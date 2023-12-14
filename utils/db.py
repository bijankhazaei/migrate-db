# DB class for get connection string and make connection and etc
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


class DB:
    def __init__(self, path, databases):
        self.target_db = None
        self.base_db = None
        self.connection_string = None
        self.path = path
        self.databases = databases
        self.create_connections()

    def create_connections(self):
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_user = os.getenv('DB_USER')
        db_pass = os.getenv('DB_PASS')
        self.connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/"
        print(self.connection_string)
        exit()
        db_names = self.databases.split("-")
        self.base_db = create_engine(self.connection_string + db_names[0])
        self.target_db = create_engine(self.connection_string + db_names[1])
