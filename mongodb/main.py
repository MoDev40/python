import pymongo

mongo = pymongo.MongoClient("mongodb://localhost:27017/")

db_list = mongo.list_database_names()
db_name = "basics"


db = mongo[db_name]

customers = "customers"
collections = db.list_collection_names()
print(collections)

customer = db[customers]


def insertOne(data: dict):
    x = customer.insert_one(data)
    print(x)


def insetMany(data: list[dict]):
    x = customer.insert_many(data)
    print(x)


# insertOne({"name": "John Doe", "address": "L33KM2"})

# insetMany([{'name':'Gomez',"address": "Mog,KM4"}])

my_customers = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"},
]

# insetMany(my_customers)

data = customer.find_one()
print(data)


def getCustomers(query: dict, limit: int = 5):
    return [x for x in customer.find(query, {"name": 1}).sort("name", 1).limit(limit)]


for x in getCustomers({"name": {"$gt": "A"}}):
    print(x)

print("---------Limit---------")
for x in getCustomers({}):
    print(x)


def deleteOne(query: dict):
    print(customer.delete_one(query))


def deleteMany(query: dict):
    print(customer.delete_many(query))


def deleteAll():
    print(customer.delete_many({}))


deleteOne({"name": "Jane Doe"})

user = db["user"]
user.insert_one({"name": "Ahmed"})
user.drop()


def updateOne(query: dict, value: dict):
    print(customer.update_one(query, value))


# updateOne({"name": "John Doe"}, {"$set": {"address": "KM4"}})
updateOne({"name": "Gomez"}, {"$set": {"address": "Rosario"}})
