from sklearn.model_selection import train_test_split

def preprocessing(df):
    df =df.dropna()

    x = df.drop("Survived",axis=1)
    y =df["Survived"]
    return train_test_split(x,y,test_size=0.2,random_state=42)