from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f'mongodb+srv://techwithtim:{password}@mycluster.vpopu.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(connection_string)

dbs = client
