from fastapi import FastAPI
from app.routes import user, vehicle
from app.database import Base, engine
from app.models import User, Vehicle

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
app.include_router(vehicle.router)

@app.get("/")
def read_root():
    return {"message": "Vehicle App API"}