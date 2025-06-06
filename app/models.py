from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    user_id: str
    user_message: str
    bot_response: str