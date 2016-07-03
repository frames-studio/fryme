import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
env = os.environ
MONGO = env["MONGO"]
print MONGO

from pymongo import MongoClient
import gridfs

client = MongoClient(MONGO)

db = client.gridfs_test
fs = gridfs.GridFS(db)
id = fs.put('This is my new file. It is teh awezum!')
fpr = fs.get(id)
print fpr.read()
