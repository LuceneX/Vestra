# services/auth_service.py
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.models.token import Token
from app.models.user import User
from app.services.email_service import send_email
from app.database import db  # MongoDB connection

# Configurations
SECRET_KEY = "your_secret_key"  # Replace with environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2 Bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Generate JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def verify_token(token: str) -> User:
    """Verify the JWT token and return the associated user."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        user_data = await db["users"].find_one({"_id": user_id})
        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")
        return User(**user_data)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Retrieve the current user based on the token."""
    return await verify_token(token)


def send_password_reset_email(user: User):
    """Send password reset email to the user."""
    token = create_access_token(data={"sub": str(user.id)}, expires_delta=timedelta(minutes=15))
    reset_link = f"http://example.com/reset-password?token={token}"
    send_email(
        to=user.email,
        subject="Password Reset",
        body=f"Click here to reset your password: {reset_link}",
    )
