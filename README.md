# 🌸 Iris Flower Classifier

A beginner-friendly **end-to-end Machine Learning application** that predicts the species of an Iris flower from its sepal and petal measurements.

This project was built to understand how an ML model moves from **training → model serialization → API → frontend → prediction**.

---

## 🚀 Features

- Train an Iris classification model using Scikit-learn
- Evaluate the model using accuracy and confusion matrix
- Save the trained model using Joblib
- FastAPI REST API for predictions
- Pydantic request validation
- Interactive Swagger API documentation
- React + Vite frontend
- Frontend ↔ Backend API integration
- Display predicted species and confidence

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   React Frontend    │
                    │      Vite           │
                    └──────────┬──────────┘
                               │
                         POST /predict
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI API      │
                    │      /predict       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Predictor Layer   │
                    │    predictor.py     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Random Forest Model │
                    │   iris_model.joblib │
                    └─────────────────────┘
```

---

## 📁 Project Structure

```text
iris-classifier/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── predictor.py
│   │   └── schemas.py
│   │
│   ├── models/
│   │   └── iris_model.joblib
│   │
│   ├── training/
│   │   └── train.py
│   │
│   ├── .venv/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 🧠 Machine Learning Model

The project uses the classic **Iris dataset** containing three flower species:

- Setosa
- Versicolor
- Virginica

### Input Features

| Feature | Description |
|---|---|
| `sepal_length` | Sepal length in cm |
| `sepal_width` | Sepal width in cm |
| `petal_length` | Petal length in cm |
| `petal_width` | Petal width in cm |

### Model

The project uses a:

**Random Forest Classifier**

The trained model is saved using Joblib:

```text
backend/models/iris_model.joblib
```

---

## 📊 Model Performance

The model was trained using an 80/20 train-test split.

### Test Accuracy

```text
96.7%
```

### Confusion Matrix

```text
[[10, 0, 0],
 [ 0, 9, 1],
 [ 0, 0,10]]
```

The model correctly classified **29 out of 30** test samples.

---

## ⚙️ Backend Setup

### 1. Navigate to backend

```powershell
cd iris-classifier\backend
```

### 2. Create virtual environment

```powershell
python -m venv .venv
```

### 3. Activate virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

Or:

```powershell
pip install scikit-learn pandas joblib fastapi uvicorn
```

### 5. Train the model

```powershell
python training\train.py
```

This creates:

```text
models\iris_model.joblib
```

### 6. Start FastAPI

```powershell
uvicorn app.main:app --reload --port 8000
```

Backend will run at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically provides Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

### Health Check

```http
GET /health
```

### Prediction

```http
POST /predict
```

Example request:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Example response:

```json
{
  "prediction": "setosa",
  "confidence": 0.978
}
```

---

## 🎨 Frontend Setup

Open a second terminal:

```powershell
cd iris-classifier\frontend
```

Install dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

---

## 🔌 Frontend ↔ Backend

The React frontend sends the flower measurements to:

```text
POST http://127.0.0.1:8000/predict
```

The backend processes the request using the trained Random Forest model.

The response is returned as JSON:

```json
{
  "prediction": "setosa",
  "confidence": 0.978
}
```

The frontend then displays the prediction and confidence.

---

## 🧪 Example

### Input

```text
Sepal Length: 5.1 cm
Sepal Width: 3.5 cm
Petal Length: 1.4 cm
Petal Width: 0.2 cm
```

### Output

```text
🌸 Iris Setosa

Confidence: 97.8%
```

---

## 🛠️ Tech Stack

### Machine Learning

- Python
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Frontend

- React
- Vite
- JavaScript
- CSS

### Development

- VS Code
- Git
- GitHub

### Planned DevOps / Cloud

- Docker
- Docker Compose
- GitHub Actions
- AWS EC2
- AWS CloudWatch

---

## 🧠 What I Learned

This project focuses on understanding an **end-to-end AI Engineering workflow**.

Key concepts:

- Dataset loading
- Train/test splitting
- ML model training
- Model evaluation
- Model serialization
- ML inference
- REST APIs
- FastAPI
- Pydantic validation
- React development
- API integration
- Frontend/backend architecture

---

## 🔮 Future Improvements

- [ ] Improve input validation
- [ ] Add automated tests
- [ ] Configure CORS properly
- [ ] Add environment variables
- [ ] Add ESLint/linting
- [ ] Dockerize backend
- [ ] Dockerize frontend
- [ ] Add Docker Compose
- [ ] Add GitHub Actions CI/CD
- [ ] Deploy backend to AWS EC2
- [ ] Add CloudWatch monitoring
- [ ] Deploy frontend
- [ ] Add production configuration

---

## ▶️ Run the Complete Application

You need **two terminals**.

### Terminal 1 — Backend

```powershell
cd iris-classifier\backend
.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```

### Terminal 2 — Frontend

```powershell
cd iris-classifier\frontend
npm run dev
```

Then open:

```text
http://localhost:5173
```

---

## 🔄 Complete Workflow

```text
                Iris Dataset
                     ↓
                train.py
                     ↓
            Random Forest Model
                     ↓
             iris_model.joblib
                     ↓
                FastAPI
                     ↓
                /predict
                     ↓
              React Frontend
                     ↓
             User Prediction
```

---

## 📌 Project Goal

The goal of this project is to understand how a machine learning model can become part of a complete software application.

Instead of stopping at:

```text
Dataset → Model → Accuracy
```

the project extends the workflow to:

```text
Dataset
   ↓
Model Training
   ↓
Model Artifact
   ↓
FastAPI
   ↓
REST API
   ↓
React Frontend
   ↓
User Prediction
```

The next stage is to extend the application with **Docker, CI/CD, AWS deployment, and monitoring**.

---

## 👩‍💻 Author

**Janhavi Kashyap**

Built as a hands-on learning project exploring:

**Machine Learning + Backend Development + Frontend Integration + AI Engineering**