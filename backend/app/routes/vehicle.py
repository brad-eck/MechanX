from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.vehicle import Vehicle, VehicleCreate
from app.crud.vehicle import create_vehicle, get_vehicles_by_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/vehicles/", response_model=Vehicle)
def create_vehicle_route(vehicle: VehicleCreate, user_id: int, db: Session = Depends(get_db)):
    return create_vehicle(db, vehicle, user_id)

@router.get("/users/{user_id}/vehicles/", response_model=list[Vehicle])
def read_vehicles(user_id: int, db: Session = Depends(get_db)):
    vehicles = get_vehicles_by_user(db, user_id)
    return vehicles