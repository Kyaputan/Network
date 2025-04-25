from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import time
DATABEASE_NAME = "Company"

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=1000)
    client.admin.command('ping')
    print("✅ Connected to MongoDB!")
    
    time.sleep(1)
    
    db = client[DATABEASE_NAME]
    collections = db.list_collection_names()
    
    print(f"📁 Collections in {DATABEASE_NAME} database:")
    for coll in collections:
        print(f" - {coll}")
        time.sleep(0.2)

except ServerSelectionTimeoutError as err:
    print("❌ Connection failed: MongoDB is unreachable.")
    print(err)
except Exception as e:
    print("❌ Connection failed with unexpected error:")
    print(e)