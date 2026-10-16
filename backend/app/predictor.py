from pathlib import Path

import joblib

from app.schemas import IrisFeatures


class Predictor:
    """Loads the trained model once and turns features into a prediction."""

    def __init__(self, model_path: Path):
        if not model_path.exists():
            raise FileNotFoundError(
                f"Model file not found at {model_path}. "
                "Run `python training/train.py` first."
            )
        artifact = joblib.load(model_path)
        self.model = artifact["model"]
        self.target_names = artifact["target_names"]

    def predict(self, features: IrisFeatures) -> tuple[str, float]:
        # The model expects a 2D list: one row per sample, columns in training order.
        row = [[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width,
        ]]
        probabilities = self.model.predict_proba(row)[0]   # e.g. [0.97, 0.02, 0.01]
        best = int(probabilities.argmax())
        return self.target_names[best], float(probabilities[best])