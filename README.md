# 🚢 Titanic Survival Prediction API – Production-Ready MLOps Project

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)

---

## 📌 Overview

This project is a **production-grade MLOps pipeline** that predicts Titanic passenger survival using Machine Learning.

It simulates a **real-world ML system** including:

* Model training & evaluation
* Experiment tracking (MLflow)
* Data drift detection (Evidently)
* API deployment (FastAPI)
* Containerization (Docker)
* CI/CD automation (Jenkins)

---

## 🏗️ System Architecture

```
User Request
     ↓
FastAPI Service
     ↓
ML Model (RandomForest)
     ↓
Prediction Response

CI/CD Flow:
GitHub → Jenkins → Train → Evaluate → Docker Build → Deploy
```

---

## ⚡ Features

* 🚀 FastAPI REST API
* 🧠 RandomForest ML Model
* 📊 MLflow Experiment Tracking
* 📉 Data Drift Detection (Evidently)
* 🔁 Automated CI/CD Pipeline (Jenkins)
* 🐳 Dockerized Deployment
* 📄 Interactive API Docs (/docs)

---

## 🛠️ Tech Stack

| Category   | Tools Used   |
| ---------- | ------------ |
| Language   | Python       |
| API        | FastAPI      |
| ML         | Scikit-learn |
| Tracking   | MLflow       |
| Monitoring | Evidently    |
| CI/CD      | Jenkins      |
| Container  | Docker       |

---

## 📂 Project Structure

```
mlops-jenkins-project/
│
├── api/                
├── src/                
├── monitoring/       
├── utils/              
├── model/              
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup

```bash
git clone https://github.com/unaidabdullah-ui/mlops-jenkins-project.git
cd mlops-jenkins-project

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt

python src/train.py

uvicorn api.app:app --reload
```

---

## 🐳 Run with Docker

```bash
docker build -t mlops-app .
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

### Prediction Endpoint

**POST /predict**

#### Input:

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

#### Output:

```json
{
  "prediction": 0
}
```

---

## 🔁 CI/CD Pipeline (Jenkins)

Pipeline stages:

1. Clone Repository
2. Install Dependencies
3. Train Model
4. Evaluate Model
5. Conditional Retraining
6. Data Drift Detection
7. Docker Build
8. Deploy Container

---

## 📈 Future Enhancements

* ✅ Model versioning
* 📊 Prometheus + Grafana monitoring
* ☁️ AWS EC2 deployment
* 🔄 CI/CD via GitHub Actions
* 🎯 Probability predictions

---

## 👨‍💻 Author

**Unaid Abdullah**

---

## ⭐ Show Your Support

If you found this project helpful, consider giving it a ⭐
