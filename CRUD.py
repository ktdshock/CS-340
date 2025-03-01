from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    
    def __init__(self, user, password):
    
        USER = user
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33078  # Explicitly set the port
        DB = 'AAC'
        COLLECTION = 'animals'
        
        """Initialize the MongoDB connection"""
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client[DB]
        self.collection = self.database[COLLECTION]

    def create(self, data):
        if data and isinstance(data, dict):
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        return False

    def read(self, query):
        try:
            result = list(self.collection.find(query))
            return result if result else []
        except Exception as e:
            print(f"Error reading from database: {e}")
            return []

    def update(self, query, new_values):
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print(f"Error updating database: {e}")
            return 0

    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting from database: {e}")
            return 0