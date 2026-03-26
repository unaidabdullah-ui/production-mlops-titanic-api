import joblib
from ingestion import load_data
from preprocessing import preprocessing

def evaluate():
    model = joblib.load("model/model.pkl")
    df = load_data()
    x_train,x_test,y_train,y_test = preprocessing(df)
    acc = model.score(x_test,y_test)
    print(f"Model Accuracy: {acc}")
if __name__ == "__main__":
    evaluate()