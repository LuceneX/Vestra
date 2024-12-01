# token.py
from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class Token(Document):
    token = StringField(unique=True, required=True)
    user_id = StringField(required=True)
    expiration_date = DateTimeField()
    created_at = DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return f"<Token(token={self.token}, user_id={self.user_id}, expiration_date={self.expiration_date})>"
