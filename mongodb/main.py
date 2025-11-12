import pymongo

mongo = pymongo.MongoClient('mongodb://localhost:27017/')

db_list = mongo.list_database_names()
db_name = 'python'

if not db_name in db_list:
    global db
    db = mongo[db_name]
    print(f'DB {db_name} not exist')

customers = 'customers'
collections = db.list_collection_names()
print(collections)

if not customers in collections:
    print(f'Collection {customers} not exists')
    db[customers]
