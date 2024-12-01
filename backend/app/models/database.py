# database.py
from mongoengine import connect

# Establish connection to MongoDB
def connect_db():
    connect('your_database_name', host='mongodb://localhost:27017')  # Use your MongoDB URI

