
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🏡 House Price Prediction — Viharatech</title>
</head>
<body>
  <header>🏡 House Price Prediction Under Viharatech Organization</header>

  <section>
    <h2>📌 Project Overview</h2>
    <p>
      A production-ready <strong>House Price Prediction</strong> web application built with
      <code>Python</code>, <code>scikit-learn</code>, and <code>Flask</code>. The model predicts house prices
      based on features such as bedrooms, bathrooms, square footage, and more.
    </p>
  </section>

  <section>
    <h2>📐 Mathematical Foundation</h2>
    <p>
      The regression equation:
      <br><br>
      <code>Price = β₀ + β₁(Bedrooms) + β₂(Bathrooms) + β₃(SqftLiving) + ... + βₙ(Features) + ε</code>
    </p>
  </section>

  <section>
    <h2>📊 Dataset Description</h2>
    <ul>
      <li>Bedrooms</li>
      <li>Bathrooms</li>
      <li>Sqft Living</li>
      <li>Sqft Lot</li>
      <li>Floors</li>
      <li>Waterfront (0/1)</li>
      <li>View (0–4)</li>
      <li>Condition (1–5)</li>
      <li>Sqft Above</li>
      <li>Sqft Basement</li>
      <li>Year Built</li>
      <li>Year Renovated</li>
      <li>City (encoded)</li>
      <li>Country (encoded)</li>
      <li>Price (USD)</li>
    </ul>
  </section>

  <section>
    <h2>🗂️ Project Structure</h2>
    <pre>
HousePricePrediction/
│── main.py             # Model training script
│── app.py              # Flask backend
│── dataset.csv         # Housing dataset
│── Model.pkl           # Trained model
│── requirements.txt    # Dependencies
│── templates/index.html# Frontend UI
│── static/             # Static assets
└── README.html         # Documentation
    </pre>
  </section>

  <section>
    <h2>⚙️ Installation & Usage</h2>
    <p>Install dependencies:</p>
    <pre><code>pip install -r requirements.txt</code></pre>
    <p>Train the model:</p>
    <pre><code>python main.py</code></pre>
    <p>Run the Flask app:</p>
    <pre><code>python app.py</code></pre>
    <p>Open in browser: <strong>http://127.0.0.1:5000/</strong></p>
  </section>

  <section>
    <h2>🎯 Sample Prediction</h2>
    <p><strong>Input:</strong> 3 Bedrooms, 2 Bathrooms, 1800 Sqft Living, Built 2005</p>
    <p><strong>Output:</strong> Predicted Price: $366,308.21</p>
  </section>

  <section>
    <h2>🖼️ Demo Screenshot</h2>
    <p>Below is a sample run of the House Price Prediction web app:</p>
    <img src="static/demo.png" alt="House Price Prediction Screenshot">
  </section>

  <section>
    <h2>🛠️ Technologies Used</h2>
    <ul>
      <li>Python 3.8+</li>
      <li>NumPy, Pandas, SciPy</li>
      <li>scikit-learn</li>
      <li>Flask</li>
      <li>Pickle</li>
      <li>HTML/CSS</li>
    </ul>
  </section>

  <section>
    <h2>📬 Contact & Support</h2>
    <p><strong>Author:</strong> S. Lakshmi Kaveri</p>
    <p>💼 LinkedIn: <a href="https://linkedin.com" target="_blank">Your LinkedIn</a></p>
    <p>🐙 GitHub: <a href="https://github.com" target="_blank">Your GitHub</a></p>
    <p>📧 Email: your.email@example.com</p>
  </section>

  <div class="footer">
    📄 License: MIT | Built with ❤️ by S. Lakshmi Kaveri
  </div>
</body>
</html>
