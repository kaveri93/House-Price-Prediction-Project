from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load only the model (since you saved just LinearRegression)
with open("Model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect form data
        features = [
            float(request.form["bedrooms"]),
            float(request.form["bathrooms"]),
            float(request.form["sqft_living"]),
            float(request.form["sqft_lot"]),
            float(request.form["floors"]),
            float(request.form["waterfront"]),
            float(request.form["view"]),
            float(request.form["condition"]),
            float(request.form["sqft_above"]),
            float(request.form["sqft_basement"]),
            float(request.form["yr_built"]),
            float(request.form["yr_renovated"]),
            int(request.form["city"]),
            int(request.form["country"])
        ]

        # Predict directly
        prediction = model.predict([features])[0]
        prediction = round(prediction, 2)

        return render_template("index.html", prediction_text=f"Predicted House Price: ${prediction}")
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)


