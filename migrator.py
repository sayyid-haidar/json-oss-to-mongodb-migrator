import pymongo
import oss2
import json

from dotenv import dotenv_values

config = dotenv_values('.env')

# Configure your OSS and MongoDB connection details
oss_access_key = config['OSS_ACCESS_KEY']
oss_access_secret = config['OSS_SECRET_KEY']
oss_endpoint = config['OSS_ENDPOINT']
oss_bucket_name = config['OSS_BUCKET_NAME']

mongodb_connection_string = config['MONGODB_URI']
mongodb_database_name = config['MONGODB_DATABASE']
mongodb_collection_name = config['MONGODB_COLLECTION']

# Initialize the OSS and MongoDB clients
oss_auth = oss2.Auth(oss_access_key, oss_access_secret)
oss_bucket = oss2.Bucket(oss_auth, oss_endpoint, oss_bucket_name)

mongodb_client = pymongo.MongoClient(mongodb_connection_string)
mongodb_database = mongodb_client[mongodb_database_name]
mongodb_collection = mongodb_database[mongodb_collection_name]

parent_directory = config['OSS_PARENT_DIRECTORY']
group_ids = config['OSS_CHILD_DIRECTORYS'].split(',')

# Retrieve the JSON files from OSS and migrate to MongoDB
def migrate_json_from_oss_to_mongodb():
    print("Migration started!")

    
    
    for group_id in group_ids:
        for obj in oss2.ObjectIterator(oss_bucket,prefix=f'{parent_directory}/{group_id}'):
            if obj.key.endswith('.json'):
                file_content = oss_bucket.get_object(obj.key).read()
                json_data = json.loads(file_content)

                # Insert JSON data into MongoDB collection
                mongodb_collection.insert_one(json_data)

                print(f"JSON data migrated to MongoDB: {obj.key}")

    print("Migration completed!")

# Call the migration function
migrate_json_from_oss_to_mongodb()
