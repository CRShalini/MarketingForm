import React, { useState } from 'react';
import './MarketingForm.css';

const MarketingForm = () => {
  const [formData, setFormData] = useState({
    business_type: '',
    target_audience: '',
    key_selling_points: ''
  });
  const [result, setResult] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('http://localhost:5000/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    });
    const data = await res.json();
    setResult(data.marketing_content);
  };

  return (
    <div className="form-container">
      <h1>Marketing Content Generator</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Business Type:
          <input
            type="text"
            name="business_type"
            value={formData.business_type}
            onChange={handleChange}
            required
          />
        </label>
        <label>
          Target Audience:
          <input
            type="text"
            name="target_audience"
            value={formData.target_audience}
            onChange={handleChange}
            required
          />
        </label>
        <label>
          Key Selling Points:
          <textarea
            name="key_selling_points"
            value={formData.key_selling_points}
            onChange={handleChange}
            required
          />
        </label>
        <button type="submit">Generate</button>
      </form>
      {result && (
        <div className="result-box">
          <h2>Generated Marketing Content:</h2>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
};

export default MarketingForm;
