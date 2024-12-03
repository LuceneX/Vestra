from fastapi import APIRouter, HTTPException, Depends
from app.services.auth_service import AuthService, get_current_user
from app.models.user import User, UserCreate, UserLogin, UserResponse
from app.models.token import Token

router = APIRouter()

# Initialize service
auth_service = AuthService()

@router.post("/users/register/", response_model=User)
async def register_user(user: UserCreate):
    try:
        return await auth_service.register_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/users/login/", response_model=Token)
async def login_user(user: UserLogin):
    token = await auth_service.login_user(user)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return token

@router.get("/users/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Retrieve the currently authenticated user's information."""
    return current_user
