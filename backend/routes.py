from fastapi import APIRouter
from schemas import UserRegister, UserLogin, MessageSchema

router = APIRouter()


@router.post("/register")
async def register(data: UserRegister):
    return {"message": "User registered successfully."}


@router.post("/login")
async def login(data: UserLogin):
    return {"message": "User login successfully."}


@router.post("/message")
async def send_message(data: MessageSchema):
    return {"message": "Message sent successfully."}