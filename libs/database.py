import pymongo
import os
from bson import json_util
from bson import ObjectId   
import bson
import json


#MONGODB_URI = os.getenv("MONGO_URI")
MONGODB_URI = os.environ.get('MONGODB_URI') 
DBS_NAME = os.environ.get('DBS_NAME')
COLLECTION_NAME = os.environ.get('COLLECTION_NAME')

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
    id = fltr['_id'] 
    oid = ObjectId(id)
    try:
        result = coll.find_one(oid)
    except pymongo.errors.PyMongoError as pe:
        data = []
        data.append({'error':pe})
        return data
    else:
        try:
            data = json.loads(bson.json_util.dumps(result))
        except bson.errors.InvalidBSON as be:
            data = []
            data.append({'error':be})
            return data
        except json.JSONDecodeError as je:
            data = []
            data.append({'error':je})
            return data
        else:
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
    id = fltr['_id'] 
    oid = ObjectId(id)
    fltr = {'_id':oid}
    try:
        result = coll.update_one(fltr, updte)
    except pymongo.errors.PyMongoError as pe:
        data = []
        data.append({'error':pe})
        return data
    else:
        return result
    
def deleteOne(fltr):
    id = fltr['_id'] 
    oid = ObjectId(id)
    fltr = {'_id': oid}
    try:
        result = coll.delete_one(fltr)
    except pymongo.errors.PyMongoError as pe:
        data = []
        data.append({'error':pe})
        return data
    else:
        return result