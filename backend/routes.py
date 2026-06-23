from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from schemas import UserRegister, UserLogin, MessageSchema
from database import SessionLocal
from models import User, Message
from config import pwd_context
from auth import create_access_token, get_current_user

router = APIRouter()


@router.post("/register")
async def register(data: UserRegister):
    async with SessionLocal() as db:
        
        result = await db.execute(
            select(User).where(User.username == data.username)
            )
        existing_user = result.scalar_one_or_none()
        
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        
        hashed_password = pwd_context.hash(data.password)
        
        new_user = User(
            name = data.name,
            username = data.username,
            password = hashed_password
        )
        
        db.add(new_user)
        await db.commit()
        
        return {"message": "User registered successfully"}



@router.post("/login")
async def login(data: UserLogin):
    async with SessionLocal() as db:
        
        result = await db.execute(
            select(User).where(User.username == data.username)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            raise HTTPException(status_code=400, detail="Username not found")
        
        if not pwd_context.verify(data.password, user.password):
            raise HTTPException(status_code=400, detail="Incorrect password")
        
        token = create_access_token({"sub": str(user.id)})
        
        return {
            "access_token": token,
            "token_type": "bearer",
            "message": "User login successfully"
            }



@router.post("/message")
async def send_message(data: MessageSchema, current_user = Depends(get_current_user)):
    return {"message": "Message sent successfully."}