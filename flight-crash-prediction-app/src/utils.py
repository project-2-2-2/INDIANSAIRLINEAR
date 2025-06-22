def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Example preprocessing steps
    df = df.dropna()  # Remove missing values
    df['crash_occurred'] = df['crash_occurred'].astype(int)  # Convert target to integer
    return df

def split_data(df, target_column):
    from sklearn.model_selection import train_test_split
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=0.4, random_state=42)

def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import accuracy_score, classification_report
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report

def save_model(model, file_path):
    import joblib
    joblib.dump(model, file_path)

def load_model(file_path):
    import joblib
    return joblib.load(file_path)