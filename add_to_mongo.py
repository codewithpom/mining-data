from pymongo import MongoClient
import json
import os
data = json.loads(open('ingredients.json').read())['meals']

password = os.getenv('PASS')

url = f"mongodb+srv://reader:{password}@cluster0.lba6uvy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client['food-info']
collection = db['ingredients']
collection.insert_many(data)

