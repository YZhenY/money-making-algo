from pymongo import MongoClient




# collection name : string, data: json format
def static_update_collection(collection_name, data, mongo_url):
	#creates connection to a local host. Needs to be changed in deployment (probably)
	client = MongoClient()

	db = client.static_data

	coll = db[collection_name]

	try:
		coll.insert_many(data)
	except:
		print("Was not able to 'insert_many' in " + collection_name)

	client.close()






