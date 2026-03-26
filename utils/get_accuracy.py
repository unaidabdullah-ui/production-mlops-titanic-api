import joblib
from ingestion import load_data
from preprocessing import preprocess

model = joblib.load("models/model.pkl")
df = load_data()
_, x_test, _, y_test = preprocess(df)

acc = model.score(x_test, y_test)

print(acc)