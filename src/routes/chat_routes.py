# Switch

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse

# chat_llm

from src.services import get_ai_response

# schema

from src.schemas import ChatRequest

chat_router = APIRouter()

@chat_router.post('/chat',status_code= status.HTTP_200_OK)
async def chat_endpoint(request: ChatRequest):
     try:
          user_msg = request.message

          user_history = request.history 

          return StreamingResponse(
               get_ai_response(user_msg, user_history),
               media_type= "text/event-stream"
          )

     except Exception as e:

          raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

