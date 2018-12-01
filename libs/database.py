import pymongo
import os


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
    recipes = []
    cursor = coll.find()
    for document in cursor:
        recipes.append(document)
    return recipes
    
def insert(doc):
    coll.insert_one(doc)
    
    
    