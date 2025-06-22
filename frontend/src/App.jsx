import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';

const fields = [
  { name: 'aircraft_type', label: 'Aircraft Type' },
  { name: 'airline', label: 'Airline' },
  { name: 'total_passengers', label: 'Total Passengers', type: 'number' },
  { name: 'crew_count', label: 'Crew Count', type: 'number' },
  { name: 'weather_condition', label: 'Weather Condition' },
  { name: 'visibility_km', label: 'Visibility (km)', type: 'number' },
  { name: 'wind_speed_kmh', label: 'Wind Speed (km/h)', type: 'number' },
  { name: 'temperature_c', label: 'Temperature (°C)', type: 'number' },
  { name: 'aircraft_age_years', label: 'Aircraft Age (years)', type: 'number' },
  { name: 'engine_condition', label: 'Engine Condition' },
  { name: 'maintenance_score', label: 'Maintenance Score', type: 'number' },
  { name: 'pilot_experience_years', label: 'Pilot Experience (years)', type: 'number' },
  { name: 'flight_duration_hours', label: 'Flight Duration (hours)', type: 'number' },
  { name: 'route_difficulty', label: 'Route Difficulty' }
];

function Home() {
  return (
    <div className="hero-bg">
      <div className="card animated-card home-card">
        <h1>✈️ Flight Crash Predictor</h1>
        <p>
          Welcome to the Flight Crash Predictor!<br />
          This tool uses machine learning to estimate the risk of a flight crash based on various flight and aircraft parameters.
        </p>
        <Link to="/predict">
          <button className="home-btn">Get Started</button>
        </Link>
      </div>
    </div>
  );
}

function Predict() {
  const [form, setForm] = useState({});
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setPrediction(null);
    try {
      const res = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      });
      const data = await res.json();
      setPrediction(data.prediction);
    } catch (err) {
      setPrediction('Error: Could not get prediction');
    }
    setLoading(false);
  };

  return (
    <div className="hero-bg">
      <div className="card animated-card" id="predict">
        <h2>Predict Flight Crash Risk</h2>
        <form onSubmit={handleSubmit}>
          {fields.map(field => (
            <div className="form-group" key={field.name}>
              <label>{field.label}:</label>
              <input
                type={field.type || 'text'}
                name={field.name}
                value={form[field.name] || ''}
                onChange={handleChange}
                required
                autoComplete="off"
              />
            </div>
          ))}
          <button type="submit" disabled={loading}>
            {loading ? 'Predicting...' : 'Predict'}
          </button>
        </form>
        {prediction && (
          <div className={`result animated-result ${prediction === 'Crash' ? 'crash' : 'no-crash'}`}>
            <h3>Prediction: {prediction}</h3>
          </div>
        )}
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <nav className="navbar">
        <div className="navbar-logo">
          <span role="img" aria-label="plane">✈️</span>
          <span className="navbar-title">Flight Crash Predictor</span>
        </div>
        <div className="navbar-links">
          <Link to="/">Home</Link>
          <Link to="/predict">Predict</Link>
          <a href="https://github.com/" target="_blank" rel="noopener noreferrer">GitHub</a>
        </div>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/predict" element={<Predict />} />
      </Routes>
      <footer className="footer">
        <span>© {new Date().getFullYear()} Flight Crash Predictor</span>
      </footer>
    </Router>
  );
}

export default App;