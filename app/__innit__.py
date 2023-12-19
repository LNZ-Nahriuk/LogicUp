from flask import  Flask
from .main import main
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
def create_app():
    app = Flask(__name__)
    myclient = pymongo.MongoClient("mongodb+srv://Nazariy:LBn2bCHbHcUngtuO@logicup.mioxl7y.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]
    app.register_blueprint(main)
    return app