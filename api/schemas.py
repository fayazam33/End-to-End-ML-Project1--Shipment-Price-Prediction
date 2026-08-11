from typing import Dict, Any
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    data: Dict[str, Any]