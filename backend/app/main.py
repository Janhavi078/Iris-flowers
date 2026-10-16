from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from app.predictor import Predictor
from app.schemas import IrisFeatures, PredictionResponse

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "iris_model.joblib"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once at startup: load the model into memory, not on every request.
    app.state.predictor = Predictor(MODEL_PATH)
    yield


app = FastAPI(title="Iris Classifier API", lifespan=lifespan)

# CORS: allow the React dev server to call this API from the browser.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict(features: IrisFeatures, request: Request):
    try:
        species, confidence = request.app.state.predictor.predict(features)
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed")
    return PredictionResponse(prediction=species, confidence=round(confidence, 4))