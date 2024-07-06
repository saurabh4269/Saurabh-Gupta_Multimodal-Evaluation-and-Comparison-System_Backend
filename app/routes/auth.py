from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token")
async def login():
    return {"access_token": "fake_token", "token_type": "bearer"}

@router.get("/users/me", dependencies=[Depends(oauth2_scheme)])
async def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"username": "fake_user"}
