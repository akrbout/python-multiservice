from pydantic import BaseModel, Field, EmailStr
from enum import Enum


class AccountRoles(Enum):
    default = "default"
    business = "business"


class User(BaseModel):
    email: EmailStr = Field()
    username: str = Field()
    full_name: str = Field(description="Имя пользователя")
    phone_num: str = Field()
    role: AccountRoles = Field(default=AccountRoles.default, description="Тип аккаунта пользователя")


class RegistrateUser(User):
    password: str = Field(min_length=8, max_length=32)


class ProfileStatus(BaseModel):
    status: bool = Field()
    message: str = Field()
