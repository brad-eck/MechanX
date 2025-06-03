from pydantic import BaseModel

class VehicleBase(BaseModel):
    year: int
    make: str
    model: str
    mileage: int
    condition: str

class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True