import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from models.neural_network import FlightCrashModel
import joblib
# ...existing code...


def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Drop columns that are not useful or are IDs/dates
    df = df.drop([
        'incident_id', 'date', 'departure_time', 'cause_category', 'fatalities'
    ], axis=1)
    
    # Separate features and target
    X = df.drop(['crash_occurred'], axis=1)
    y = df['crash_occurred']
    
    # Identify categorical and numeric columns
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    # Build a preprocessing pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
        ]
    )
    return X, y, preprocessor
import joblib
# ...existing code...
from imblearn.over_sampling import SMOTE

# ...existing code...

def main():
    data = load_data('./data/incidents.csv')
    X, y, preprocessor = preprocess_data(data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Fit preprocessor on training data only
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)
    
    # Oversample the minority class
    X_train_bal, y_train_bal =  X_train_processed, y_train
    
    model = FlightCrashModel()
    model.fit(X_train_bal, y_train_bal)
    print("Training complete.")
    print("Test accuracy:", model.model.score(X_test_processed, y_test))

    # Save the trained model and preprocessor
    joblib.dump(model.model, 'models/trained_flight_crash_model.pkl')
    joblib.dump(preprocessor, 'models/preprocessor.pkl')
if __name__ == "__main__":
    main()
