from pydantic import BaseModel, EmailStr, Field

class Doctor(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True

class Patient(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    phone: str
