from pydantic import BaseModel,Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category:str=Field(...,description="The predicted Employee Attrition",example="Yes")