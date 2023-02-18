import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongodb_connection = os.getenv('MONGODB_CONNECT_URL')


class DBUtility:
    def __init__(self):
        self.client = MongoClient(mongodb_connection)
        self.database = self.client['test-food-shop']
        self.users = self.database['users']
        self.tokens = self.database['tokens']
        self.fooditems = self.database['fooditems']
        self.foodsections = self.database['foodsections']

    def clear_database(self):
        self.users.delete_many({})
        self.tokens.delete_many({})
        self.fooditems.delete_many({})
        self.foodsections.delete_many({})
