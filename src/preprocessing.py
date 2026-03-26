import pandas as pd
from sklearn.model_selection import train_test_split

def preprocessing(df):
    # Drop missing values
    df = df.dropna()

    # Drop unnecessary columns
    df = df.drop(['Name', 'Ticket', 'Cabin'], axis=1)

    # Features and target
    x = df.drop('Survived', axis=1)
    y = df['Survived']

    # Convert categorical to numeric
    x = pd.get_dummies(x, columns=['Sex', 'Embarked'], drop_first=True)

    # Train-test split
    return train_test_split(x, y, test_size=0.2, random_state=42)
