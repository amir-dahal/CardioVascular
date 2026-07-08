from pydantic import BaseModel
 
class Cardio(BaseModel):
    age: int
    gender: int
    height: float
    weight: int
    ap_hi: int
    ap_lo: int
    cholesterol: int
    gluc: int
    smoke: int
    alco: int
    active: int