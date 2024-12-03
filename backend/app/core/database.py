from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(settings.database_url)
db = client["ecommerce_db"]
