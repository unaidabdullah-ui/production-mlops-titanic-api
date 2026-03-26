# 🚢 Titanic Survival Prediction API (MLOps Project)

A production-ready **Machine Learning API** built using **FastAPI, Docker, and Scikit-learn** to predict whether a passenger would survive the Titanic disaster.

---

## 🚀 Features

* ⚡ FastAPI-based REST API
* 🧠 Machine Learning model (Scikit-learn)
* 🐳 Dockerized for easy deployment
* 📊 End-to-End ML pipeline (training → prediction)
* 🔍 Swagger UI for testing (`/docs`)
* 📦 Clean project structure

---

## 🛠️ Tech Stack

* Python 3.10+
* FastAPI
* Scikit-learn
* Pandas
* Joblib
* Docker
* Uvicorn

---

## 📂 Project Structure

```
mlops-jenkins-project/
│
├── api/
│   └── app.py              # FastAPI application
│
├── src/
│   └── train.py            # Model training script
│
├── model/
│   └── model.pkl           # Trained model
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/mlops-jenkins-project.git
cd mlops-jenkins-project
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run training

```bash
python src/train.py
```

### 5️⃣ Run API

```bash
uvicorn api.app:app --reload
```

---

## 🐳 Run with Docker

### Build image

```bash
docker build -t mlops-app .
```

### Run container

```bash
docker run -p 8000:8000 mlops-app
```

---

## 🌐 API Usage

### Base URL

```
http://localhost:8000
```

### Swagger Docs

```
http://localhost:8000/docs
```

---

## 🔮 Prediction Endpoint

### POST `/predict`

### Example Request

```json
{
  "PassengerId": 1,
  "Pclass": 3,
  "Age": 22,
  "SibSp": 0,
  "Parch": 0,
  "Fare": 7.25,
  "Sex_male": 1,
  "Embarked_Q": 0,
  "Embarked_S": 1
}
```

### Example Response

```json
{
  "prediction": 0
}
```

* `0` → Did not survive
* `1` → Survived

---

## 🧠 ML Pipeline

1. Data preprocessing
2. Feature engineering (encoding, cleaning)
3. Model training (RandomForestClassifier)
4. Model saving using Joblib
5. API serving predictions

---

## ⚠️ Important Notes

* Input must match **trained feature format**
* Model expects **preprocessed features**
* Do NOT include `venv/` or large files in repo

---

## 🚀 Future Improvements

* ✅ Add full preprocessing pipeline (no manual encoding)
* ✅ Add prediction probability (`predict_proba`)
* ✅ Integrate MLflow for tracking
* ✅ CI/CD with Jenkins / GitHub Actions
* ✅ Deploy on AWS (EC2 / Docker)

---

## 👨‍💻 Author

**Unaid Abdullah**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it 🚀
