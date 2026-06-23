from dotenv import load_dotenv
from passlib.context import CryptContext 
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24*7

pwd_context = CryptContext(schemes=["argon2"])