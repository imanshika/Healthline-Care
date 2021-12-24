from pydantic import BaseModel

# Diabeties Features
class diabetes(BaseModel):
    pregnancies: int 
    glucose: int
    bloodPressure: int
    skinThickness: int
    insulin: int
    bmi: float
    diabetesPedigreeFunction: float
    age: int