from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    nome: str
    email: EmailStr
    password: str
    
class UserPublic(BaseModel):
    id: int
    nome: str
    email: EmailStr
    
class UserDB(BaseModel):
    id: int
    nome: str
    email: EmailStr
    
class UserList(BaseModel):
    users: list[UserPublic]