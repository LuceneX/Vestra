from fastapi import APIRouter, HTTPException
from app.services.auth_service import AuthService
from app.models.user import User, UserCreate, UserLogin
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

@router.get("/users/me/", response_model=User)
async def get_current_user(user: User = Depends(get_current_user)):
    return user
