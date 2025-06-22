import pandas as pd
import numpy as np
import joblib
from models.neural_network import FlightCrashModel
    
def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Implement necessary preprocessing steps
    data = data.drop(columns=['incident_id', 'date'])  # Example of dropping non-predictive columns
    data = pd.get_dummies(data, drop_first=True)  # Convert categorical variables to dummy variables
    return data

def make_predictions(model, data):
    predictions = model.predict(data)
    return predictions
def main():
    # Load the preprocessor and model
    preprocessor = joblib.load('models/preprocessor.pkl')
    model = joblib.load('models/trained_flight_crash_model.pkl')

    # Load and preprocess new data
    data = load_data('data/incidents.csv')
    if 'crash_occurred' in data.columns:
        data = data.drop(['crash_occurred'], axis=1)
    processed_data = preprocessor.transform(data)
    
    # Get probabilities for the "Crash" class (usually class 1)
    probas = model.predict_proba(processed_data)
    crash_probs = probas[:, 1]  # Assuming class 1 is "Crash"

    predictions = (crash_probs > 0.3).astype(int)
    print("Predictions:", predictions)
    

if __name__ == "__main__":
    main()