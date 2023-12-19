from flask import Blueprint
from .extensions import mongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
main = Blueprint('main',__name__)

@main.route('/')
def index():
    
    
    return user