import { useState } from "react";
import "./App.css";

const API_URL = "http://localhost:8000";

const FIELDS = [
  { name: "sepal_length", label: "Sepal Length (cm)" },
  { name: "sepal_width", label: "Sepal Width (cm)" },
  { name: "petal_length", label: "Petal Length (cm)" },
  { name: "petal_width", label: "Petal Width (cm)" },
];

export default function App() {
  const [values, setValues] = useState({
    sepal_length: "5.1",
    sepal_width: "3.5",
    petal_length: "1.4",
    petal_width: "0.2",
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState(null);

  function handleChange(e) {
    setValues({ ...values, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");
    setResult(null);

    // Client-side check: every field must be a positive number.
    const payload = {};
    for (const { name, label } of FIELDS) {
      const num = parseFloat(values[name]);
      if (values[name].trim() === "" || Number.isNaN(num) || num <= 0) {
        setError(`${label} must be a positive number.`);
        return;
      }
      payload[name] = num;
    }

    setLoading(true);
    try {
      const response = await fetch(`${API_URL}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await response.json();

      if (!response.ok) {
        // FastAPI validation errors (422) have detail as a list.
        if (Array.isArray(data.detail)) {
          setError(
            data.detail.map((d) => `${d.loc[d.loc.length - 1]}: ${d.msg}`).join("; ")
          );
        } else {
          setError(data.detail || "Something went wrong.");
        }
        return;
      }
      setResult(data);
    } catch {
      // fetch throws only when the request never got a response (backend down, CORS, etc.)
      setError("Cannot reach the backend. Is it running on http://localhost:8000?");
    } finally {
      setLoading(false);
    }
  }

  const speciesName = result
    ? `Iris ${result.prediction[0].toUpperCase()}${result.prediction.slice(1)}`
    : "";

  return (
    <div className="page">
      <form className="card" onSubmit={handleSubmit}>
        <h1>Iris Flower Classifier</h1>
        <p className="subtitle">Enter the flower measurements and predict its species.</p>

        {FIELDS.map(({ name, label }) => (
          <label className="field" key={name}>
            <span>{label}</span>
            <input
              name={name}
              type="number"
              step="0.1"
              value={values[name]}
              onChange={handleChange}
              disabled={loading}
            />
          </label>
        ))}

        <button type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Predict"}
        </button>

        {error && <div className="error">{error}</div>}

        {result && (
          <div className="result">
            <p className="result-label">Prediction:</p>
            <p className="result-value">🌸 {speciesName}</p>
            <p className="result-label">Confidence:</p>
            <p className="result-value">{(result.confidence * 100).toFixed(1)}%</p>
          </div>
        )}
      </form>
    </div>
  );
}