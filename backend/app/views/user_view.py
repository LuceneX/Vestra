from fastapi import APIRouter, Depends, HTTPException, status
from app.services.auth_service import AuthService
from app.models.user import User, UserCreate, Token
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

# Dependency injection for AuthService
def get_auth_service() -> AuthService:
    return AuthService()

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, service: AuthService = Depends(get_auth_service)):
    """Register a new user."""
    created_user = await service.register_user(user)
    if not created_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Registration failed")
    return created_user

@router.post("/login", response_model=Token)
async def login_user(username: str, password: str, service: AuthService = Depends(get_auth_service)):
    """Authenticate a user and return a token."""
    token = await service.authenticate_user(username, password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return token

@router.get("/", response_model=List[User])
async def list_users(service: AuthService = Depends(get_auth_service)):
    """Get a list of all users."""
    return await service.get_all_users()

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str, service: AuthService = Depends(get_auth_service)):
    """Get a user by ID."""
    user = await service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, service: AuthService = Depends(get_auth_service)):
    """Delete a user."""
    success = await service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"message": "User deleted successfully"}
