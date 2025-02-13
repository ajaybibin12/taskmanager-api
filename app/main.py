from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# MongoDB Connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://admin:adminpass@mongo_container:27017/")
client = MongoClient(MONGO_URL)
db = client.taskmanager

@app.get("/")
def home():
    return {"message": "Task Manager API Running Successfully"}

@app.get("/tasks")
def get_tasks():
    tasks = list(db.tasks.find({}, {"_id": 0}))  # Return tasks without _id field
    return {"tasks": tasks}
