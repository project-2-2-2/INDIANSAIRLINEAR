from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")

# Serve React build
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

# ...your API routes...
CORS(app)  # Allow React frontend to access the API

model = joblib.load('../models/trained_flight_crash_model.pkl')
preprocessor = joblib.load('../models/preprocessor.pkl')

FIELDS = [
    'aircraft_type', 'airline', 'total_passengers', 'crew_count', 'weather_condition',
    'visibility_km', 'wind_speed_kmh', 'temperature_c', 'aircraft_age_years',
    'engine_condition',  # <-- Add this line
    'maintenance_score', 'pilot_experience_years', 'flight_duration_hours',
    'route_difficulty'
]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = {field: data[field] for field in FIELDS}
    for key in ['total_passengers', 'crew_count', 'visibility_km', 'wind_speed_kmh',
                'temperature_c', 'aircraft_age_years', 'maintenance_score',
                'pilot_experience_years', 'flight_duration_hours']:
        input_data[key] = float(input_data[key])
    df = pd.DataFrame([input_data])
    X = preprocessor.transform(df)
    pred = model.predict(X)[0]
    return jsonify({'prediction': 'Crash' if pred == 1 else 'No Crash'})

if __name__ == '__main__':
    app.run(debug=True)