from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.database.session import get_db
from app.models.user import User
from app.dependencies import get_current_user
from app.config import settings
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    name: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "securePassword123",
                "name": "John Doe"
            }
        }

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "securePassword123"
            }
        }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "Bearer",
                "expires_in": 3600
            }
        }

@router.post("/register", 
    summary="Register a new user",
    description="Create a new user account with email and password",
    response_description="User created successfully"
)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new user account:
    
    - **email**: Valid email address (must be unique)
    - **password**: User password (will be hashed)
    - **name**: User's full name
    
    Returns the created user's ID, email, and role.
    """
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(request.password)
    user = User(
        email=request.email,
        password_hash=hashed_password,
        role="manager"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return {
        "user_id": str(user.id),
        "email": user.email,
        "role": user.role
    }

@router.post("/login", 
    response_model=TokenResponse,
    summary="User login",
    description="Authenticate user and receive JWT access token"
)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Authenticate with email and password:
    
    - **email**: Registered email address
    - **password**: User password
    
    Returns a JWT access token for authenticated requests.
    """
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not pwd_context.verify(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode(
        {"sub": str(user.id), "exp": datetime.utcnow() + access_token_expires},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    
    return {
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }

@router.post("/logout")
async def logout():
    return {"message": "Logged out successfully"}

@router.post("/forgot-password")
async def forgot_password(email: EmailStr):
    return {"message": "Password reset email sent"}

@router.post("/reset-password")
async def reset_password():
    return {"message": "Password reset successful"}

@router.get("/me",
    summary="Get current user",
    description="Retrieve authenticated user's profile information"
)
async def get_me(current_user: User = Depends(get_current_user)):
    """
    Get the current authenticated user's profile.
    
    Requires valid JWT token in Authorization header.
    """
    return {
        "user_id": str(current_user.id),
        "email": current_user.email,
        "role": current_user.role,
        "created_at": current_user.created_at.isoformat()
    }
