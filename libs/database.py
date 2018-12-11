import pymongo
import os
from bson import json_util
import bson
import json


#MONGODB_URI = os.getenv("MONGO_URI")
MONGODB_URI = 'mongodb://root:IflsMF01@ds211504.mlab.com:11504/code-institute-data-centric'
DBS_NAME = "code-institute-data-centric"
COLLECTION_NAME = "recipeDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

def find():
    try:
        cursor = coll.find()
    except pymongo.errors.PyMongoError as pe:
        data = []
        data.append({'error':pe})
        return data
    else:
        try:
            data=json.loads(bson.json_util.dumps(cursor))
            return data
        except bson.errors.InvalidBSON as be:
            data = []
            data.append({'error':be})
            return data
        except json.JSONDecodeError as je:
            data = []
            data.append({'error':je})
            return data

def findOne(fltr):
    try:
        result = coll.find_one(fltr)
    except pymongo.errors.PyMongoError as pe:
        data = []
        data.append({'error':pe})
        return data
    else:
        try:
            data = json.loads(bson.json_util.dumps(result))
            return data
        except bson.errors.InvalidBSON as be:
            data = []
            data.append({'error':be})
            return data
        except json.JSONDecodeError as je:
            data = []
            data.append({'error':je})
            return data

def insert(doc):
    try:
        result = coll.insert_one(doc)
    except pymongo.errors.PyMongoError as pe:
        data = []
        data.append({'error':pe})
        return data
    else:
        return result

def updateOne(fltr, updte):
    try:
        result = coll.update_one(fltr, updte)
    except pymongo.errors.PyMongoError as pe:
        data = []
        data.append({'error':pe})
        return data
    else:
        return result
    
def deleteOne(fltr):
    try:
        result = coll.delete_one(fltr)
    except pymongo.errors.PyMongoError as pe:
        data = []
        data.append({'error':pe})
        return data
    else:
        return result