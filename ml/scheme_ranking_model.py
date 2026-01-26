import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

def train_ranking_model(csv_path):
    df = pd.read_csv(csv_path)

    le_state = LabelEncoder()
    le_category = LabelEncoder()

    df["state_enc"] = le_state.fit_transform(df["state"])
    df["category_enc"] = le_category.fit_transform(df["category"])

    X = df[["min_income", "max_income", "min_age", "max_age", "state_enc", "category_enc"]]
    y = [1] * len(df)  # placeholder relevance labels

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    return model
