# Date 10/18/2026
# Name:Anthony Flores
# Version 0.4
# SNHU CS-340-14096-M01 Client/Server Development
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
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # method to implement the C in CRUD. 
    def create(self, data):
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e: # Handle errors while inserting into MongoDB
                print("Error has occurred", e)
                return False
            else:
                return False
    # method to implement the R in CRUD.
    # updated Read Method
    def read(self, query):
        try:
            results = self.collection.find(query)
            return list(results)
        except Exception as e: # Handle errors while querying MongoDB
            print("Error has occurred:", e)
            return []
    
    # Method to implement the U in CRUD
    def update(self, query, update_data):
        if query and update_data:
            try:
                result = self.collection.update_many(query, {"$set": update_data})
                return result.modified_count
            except Exception as e: # Handle errors while updating MonogDB
                print("Error has occurred:", e)
                return 0
        else:
            return 0
    
    # Method to implement the D in CRUD
    def delete(self, query):
        if query:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e: # Handle errors while deleting from MonogDB
                print("Error has occurred:", e)
                return 0
        else:
            return 0
