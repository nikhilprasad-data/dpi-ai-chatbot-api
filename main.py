# fastapi

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# routes

from src.routes import chat_router

app = FastAPI()

app.add_middleware(
     CORSMiddleware,
     allow_origins  = ["http://localhost:3000",""],
     allow_credentials= True,
     allow_methods    = ["*"],
     allow_headers    = ["*"]
)

app.include_router(chat_router, prefix= "/api", tags= ["chat_router"])
