# services/auth_service.py
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from app.models.token import Token
from app.models.user import User
from app.services.email_service import send_email

SECRET_KEY = "your_secret_key"  # Change this in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiry time

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Generate JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """Verify the token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = User.objects.get(id=payload["sub"])  # Assuming "sub" is user ID
        return user
    except JWTError:
        return None

def send_password_reset_email(user: User):
    """Send password reset email to the user."""
    token = create_access_token(data={"sub": str(user.id)}, expires_delta=timedelta(minutes=15))
    reset_link = f"http://example.com/reset-password?token={token}"
    send_email(to=user.email, subject="Password Reset", body=f"Click here to reset your password: {reset_link}")
