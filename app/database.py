from pymongo import MongoClient
from app.config import MONGODB_URI, DATABASE_NAME
from datetime import datetime

class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[DATABASE_NAME]
        self.conversations = self.db.conversations

    def save_conversation(self, user_id: str, user_message: str, bot_response: str):
        conversation = {
            "user_id": user_id,
            "user_message": user_message,
            "bot_response": bot_response,
            "timestamp": datetime.utcnow()
        }
        self.conversations.insert_one(conversation)

    def get_conversation_history(self, user_id: str, limit: int = 10):
        return list(self.conversations.find({"user_id": user_id}).sort("timestamp", -1).limit(limit))

mongo_db = MongoDB()