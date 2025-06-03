from sqlalchemy.orm import Session
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate

def create_vehicle(db: Session, vehicle: VehicleCreate, user_id: int):
    db_vehicle = Vehicle(**vehicle.dict(), user_id=user_id)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def get_vehicles_by_user(db: Session, user_id: int):
    return db.query(Vehicle).filter(Vehicle.user_id == user_id).all()