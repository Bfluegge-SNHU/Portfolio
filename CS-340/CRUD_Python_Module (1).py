# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if not isinstance(data, dict) or not data:
            return False

        try:
            result = self.collection.insert_one(data)
            return result.acknowledged

        except PyMongoError as error:
            print("Create operation failed:", error)
            return False

    # Create method to implement the R in CRUD.
    
    def read(self, query):

        if not isinstance(query, dict):
            return []

        try:
            cursor = self.collection.find(query)
            return list(cursor)

        except PyMongoError as error:
            print("Read operation failed:", error)
            return [] 
        
        
    def update(self, query, new_values):
        if query and new_values:
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": new_values}
                )
                return result.modified_count
            except Exception as e:
                print(f"Update error: {e}")
                return 0
        return 0


    def delete(self, query):
        if query:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"Delete error: {e}")
                return 0
        return 0