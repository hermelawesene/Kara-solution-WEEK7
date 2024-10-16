# schemas.py

from pydantic import BaseModel

class DetectionBase(BaseModel):
    img_name: str
    object_name: str
    confidence: float
    x_min: float
    y_min: float
    x_max: float
    y_max: float

class DetectionCreate(DetectionBase):
    pass

class Detection(DetectionBase):
    id: int

    class Config:
        orm_mode = True
