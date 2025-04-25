from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import datetime
import random

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=1000)
    client.admin.command('ping')
    print("✅ Connected to MongoDB!")

    db = client['Company']

    db.employees.delete_many({})
    db.sela.delete_many({})
    db.Matedata.delete_many({})

    employee_names = [
    "John Doe", "Alice Smith", "Bob Johnson", "Emily Davis", "Michael Lee",
    "Sarah Brown", "David Wilson", "Linda Martinez", "James Anderson", "Karen Thomas",
    "Chris Moore", "Patricia Taylor", "Daniel White", "Nancy Harris", "Mark Martin",
    "Barbara Thompson", "Steven Garcia", "Susan Clark", "Paul Rodriguez", "Jessica Lewis",
    "Andrew Walker", "Laura Hall", "Kevin Allen", "Michelle Young", "Brian King",
    "Lisa Wright", "Jason Scott", "Angela Green", "Matthew Adams", "Rebecca Baker"
]

    product_types = [
        "หูฟัง", "เมาส์", "คีย์บอร์ด", "โน้ตบุ๊ก", "จอภาพ", 
        "เครื่องพิมพ์", "ลำโพง", "แฟลชไดรฟ์", "กล้องเว็บแคม", "แท็บเล็ต"
    ]

    thai_provinces = [
        "เชียงใหม่", "เชียงราย", "ลำปาง", "แพร่", "น่าน",
        "ขอนแก่น", "อุบลราชธานี", "นครราชสีมา", "อุดรธานี", "มหาสารคาม",
        "กรุงเทพมหานคร", "นนทบุรี", "พระนครศรีอยุธยา", "สระบุรี", "สมุทรปราการ",
        "ชลบุรี", "ระยอง", "จันทบุรี", "ตราด", "ปราจีนบุรี",
        "ภูเก็ต", "สุราษฎร์ธานี", "สงขลา", "นครศรีธรรมราช", "กระบี่"
    ]


    for i, name in enumerate(employee_names):
        employee = {
            "name": name,
            "position": "Sales",
            "employee_id": f"E00{i+1}",
            "hire_date": datetime.datetime.now()
        }
        emp_id = db.employees.insert_one(employee).inserted_id

        # สร้างสินค้า 2 อันต่อพนักงาน
        for j in range(5):
            product_name = random.choice(product_types)
            sela = {
                "product_name": product_name,
                "price": random.randint(500, 50000),
                "sold_by": emp_id,
                "Name": name,
            }
            sela_id = db.sela.insert_one(sela).inserted_id

            # Metadata
            shipped_at = datetime.datetime.now()
            expected_arrival = shipped_at + datetime.timedelta(days=random.randint(2, 3))
            metadata = {
                "sela_id": sela_id,
                "destination": random.choice(thai_provinces),
                "shipped_at": shipped_at,
                "expected_arrival": expected_arrival
            }
            db.Matedata.insert_one(metadata)

    print("✅ Data for 5 employees, products, and metadata inserted successfully.")

except ServerSelectionTimeoutError as err:
    print("❌ Connection failed: MongoDB is unreachable.")
    print(err)
except Exception as e:
    print("❌ Connection failed with unexpected error:")
    print(e)



# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://root:310146@mycluster.porewyk.mongodb.net/?appName=MyCluster"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
#     db = client["sample_mflix"]
#     collections = db.list_collection_names()
#     for collection in collections:
#         print(collection)
        
# except Exception as e:
#     print(e)