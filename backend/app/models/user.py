# user.py
from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class User(Document):
    user_id = StringField(primary_key=True)
    username = StringField(unique=True, required=True)
    email = StringField(unique=True, required=True)
    password_hash = StringField(required=True)
    role = StringField(default='user')
    created_at = DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username}, email={self.email})>"
