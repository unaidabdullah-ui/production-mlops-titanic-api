import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from ingestion import load_data
from preprocessing import preprocessing
import joblib

mlflow.set_experiment("Titanic Survival Prediction")

def train():
    df = load_data()
    x_train,x_test,y_train,y_test = preprocessing(df)

    model = RandomForestClassifier()
    model.fit(x_train,y_train)

    acc = model.score(x_test,y_test)

    joblib.dump("model/model.pkl")

    with mlflow.start_run():
        mlflow.log_param("model","RandomForestClassifier")
        mlflow.log_metric("accuracy",acc)
        mlflow.sklearn.log_model(model,"model")

    print(f"Model Accuracy: {acc}")

if __name__ == "__main__":
    train()