from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from .user import User

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    year = Column(Integer)
    make = Column(String)
    model = Column(String)
    mileage = Column(Integer)
    condition = Column(String)
    user = relationship("User", back_populates="vehicles")

User.vehicles = relationship("Vehicle", order_by=Vehicle.id, back_populates="user")