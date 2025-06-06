from fastapi import FastAPI
from app.models import ChatRequest, ChatResponse
from app.chatbot import chatbot
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="E-commerce Customer Support Chatbot")

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the index.html file
@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    bot_response = chatbot.generate_response(request.user_id, request.message)
    return ChatResponse(
        user_id=request.user_id,
        user_message=request.message,
        bot_response=bot_response
    )