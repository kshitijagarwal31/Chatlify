from fastapi import APIRouter, HTTPException, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy import select
from schemas import UserRegister, UserLogin, MessageSchema
from database import SessionLocal
from models import User, Message
from config import pwd_context
from auth import create_access_token, get_current_user
from ws_manager import manager


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
            "message": "User login successfully",
            "user_id": user.id
            }



@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"User {user_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"User {user_id} left the chat")



@router.post("/message")
async def send_message(data: MessageSchema, current_user = Depends(get_current_user)):
    async with SessionLocal() as db:
        
        new_message = Message(
            sender_id = current_user.id,
            content = data.content
        )
        db.add(new_message)
        await db.commit()
        
        await manager.broadcast(f"{current_user.name}: {data.content}")
        
        return {"message": "Message sent successfully"}