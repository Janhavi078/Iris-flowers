"""Train the Iris classifier and save it to disk.

Run from the backend/ folder:
    python training/train.py
"""
from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "iris_model.joblib"


def main() -> None:
    # 1. Load data
    iris = load_iris()
    X = iris.data      # features: shape (150, 4)
    y = iris.target    # target: 0 = setosa, 1 = versicolor, 2 = virginica

    # 2. Split BEFORE training so the test set stays unseen (avoids data leakage).
    #    stratify=y keeps the class proportions equal in both sets.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Train
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # 4. Evaluate on the unseen test set
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.3f}\n")
    print("Confusion matrix (rows = true, columns = predicted):")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    # 5. Save the model together with its metadata in one file
    artifact = {
        "model": model,
        "target_names": list(iris.target_names),
        "feature_names": list(iris.feature_names),
        "accuracy": float(accuracy),
    }
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, MODEL_PATH)
    print(f"\nModel saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()