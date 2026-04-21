# 🚢 Titanic Survival Prediction API (Production-Ready MLOps Project)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

A **production-grade Machine Learning API** built using **FastAPI, Docker, and Jenkins CI/CD**, designed to simulate real-world MLOps workflows.

---

## 🚀 Project Overview

This project predicts whether a passenger survived the Titanic disaster using a trained ML model.

It demonstrates:

* End-to-end ML pipeline
* API deployment
* Containerization
* CI/CD automation using Jenkins

---

## 🏗️ Architecture

```
User → FastAPI → ML Model → Prediction
            ↓
        Docker Container
            ↓
        Jenkins Pipeline (CI/CD)
```

---

## ⚡ Features

* ⚡ FastAPI REST API
* 🧠 ML model (RandomForest)
* 🐳 Dockerized application
* 🔁 Jenkins CI/CD pipeline
* 📊 Swagger UI (`/docs`)
* 📦 Clean modular structure

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* Docker
* Jenkins
* Uvicorn

---

## 📂 Project Structure

```
mlops-jenkins-project/
│
├── api/                
├── src/                
├── model/            
├── monitoring/         
├── Jenkinsfile        
├── Dockerfile
└── requirements.txt
```

---

## ⚙️ Local Setup

```bash
git clone https://github.com/your-username/mlops-jenkins-project.git
cd mlops-jenkins-project

python3 -m venv venv
source venv/bin/activate

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

## 🌐 API Endpoints

### Base URL

```
http://localhost:8000
```

### Swagger Docs

```
http://localhost:8000/docs
```

---

## 🔮 Prediction API

### POST `/predict`

### Example Input:

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

### Response:

```json
{
  "prediction": 0
}
```

---

## 🔁 CI/CD Pipeline (Jenkins)

Pipeline stages:

1. Code Pull from GitHub
2. Install Dependencies
3. Train Model
4. Build Docker Image
5. Run Container

👉 Fully automated deployment using Jenkinsfile

---

## 📈 Future Improvements

* Add MLflow tracking
* Add model versioning
* Add monitoring (Prometheus/Grafana)
* Deploy on AWS EC2
* Add prediction probabilities

---

## 👨‍💻 Author

**Unaid Abdullah**

---

## ⭐ Support

If you found this useful, give it a ⭐ and share 🚀
