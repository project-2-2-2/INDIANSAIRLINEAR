# Flight Crash Prediction Application

This project aims to predict flight crashes using a neural network model based on various parameters related to flight incidents. The application utilizes a dataset containing detailed information about past flight incidents to train the model and make predictions.

## Project Structure

- **data/incidents.csv**: Contains the dataset with flight incident details, including parameters such as incident_id, date, aircraft_type, airline, total_passengers, crew_count, weather_condition, visibility_km, wind_speed_kmh, temperature_c, aircraft_age_years, engine_condition, maintenance_score, pilot_experience_years, flight_duration_hours, departure_time, route_difficulty, crash_occurred, fatalities, and cause_category.

- **models/neural_network.py**: Defines the neural network model for predicting flight crashes. It includes classes and functions for building, training, and evaluating the model.

- **notebooks/exploratory_analysis.ipynb**: A Jupyter notebook for exploratory data analysis (EDA) on the flight incident dataset. It includes visualizations and statistical summaries to better understand the data.

- **src/train.py**: Contains the code for training the neural network model. It imports the dataset, preprocesses the data, and trains the model using the specified parameters.

- **src/predict.py**: Responsible for making predictions using the trained neural network model. It loads the model and the dataset, processes the input data, and outputs the predictions regarding flight crashes.

- **src/utils.py**: Includes utility functions for data preprocessing, model evaluation, and other helper functions used throughout the project.

- **requirements.txt**: Lists the dependencies required for the project, including libraries for data manipulation, machine learning, and visualization.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flight-crash-prediction-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

- To train the model, run:
  ```
  python src/train.py
  ```

- To make predictions, run:
  ```
  python src/predict.py
  ```

- For exploratory data analysis, open the Jupyter notebook:
  ```
  jupyter notebook notebooks/exploratory_analysis.ipynb
  ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.