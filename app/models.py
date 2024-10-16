# models.py

from sqlalchemy import Column, Integer, String, Float
from database import Base

class Detection(Base):
    __tablename__ = 'detections'

    id = Column(Integer, primary_key=True, index=True)
    img_name = Column(String, index=True)
    object_name = Column(String)
    confidence = Column(Float)
    x_min = Column(Float)
    y_min = Column(Float)
    x_max = Column(Float)
    y_max = Column(Float)
