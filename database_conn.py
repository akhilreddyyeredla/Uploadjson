import pymongo
def connection():
    mongo_client = pymongo.MongoClient('localhost', 27017)
    mongo_db = mongo_client['crul']  # Replace mongo db name
    collection_name = 'curl_data'  # Replace mongo db collection name
    db_connection = mongo_db[collection_name]

    return db_connection

