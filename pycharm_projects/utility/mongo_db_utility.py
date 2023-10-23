import pymongo

class mongo_db_utility:

    def __init__(self):
        global sequence
        global db
        global collection
        global client

        # Connect to your MongoDB server (modify the connection string as needed)
        client = pymongo.MongoClient("mongodb://localhost:27017/")

        # Select the database and collection
        db = client["your_database_name"]
        collection = db["your_collection_name"]



        # Create a sequence collection to hold the auto-incrementing values
        sequence = db["sequence_collection"]

        print("MongoDB utility object created.")


    # Function to get the next auto-increment value
    def get_next_sequence_value(self, sequence_name):
        sequence_doc = sequence.find_one_and_update(
            {"_id": sequence_name},
            {"$inc": {"sequence_value": 1}},
            upsert=True,
            return_document=pymongo.ReturnDocument.AFTER,
        )
        return sequence_doc["sequence_value"]

    def insert_into_tableOne(self, cart_id):
        auto_incrementing_id = self.get_next_sequence_value("tableOne_sequnce")
        data = {
            "id": auto_incrementing_id,
            "cart_id": cart_id
        }
        collection.insert_one(data)

        # Close the MongoDB connection
        client.close()
