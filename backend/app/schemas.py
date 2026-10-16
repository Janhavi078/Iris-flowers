from pydantic import BaseModel, Field


class IrisFeatures(BaseModel):
    """Request body for /predict. Pydantic validates it automatically."""
    sepal_length: float = Field(..., gt=0, le=15, description="cm")
    sepal_width: float = Field(..., gt=0, le=15, description="cm")
    petal_length: float = Field(..., gt=0, le=15, description="cm")
    petal_width: float = Field(..., gt=0, le=15, description="cm")


class PredictionResponse(BaseModel):
    prediction: str
    confidence: float