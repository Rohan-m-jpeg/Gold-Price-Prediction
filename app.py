from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Define feature order (MUST match training order)
FEATURE_ORDER = ['SPX', 'USO', 'SLV', 'EURUSD']

# Home route (health check)
@app.route('/', methods=['GET'])
def home():
    return "Gold Price Prediction API is running"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Extract features in correct order
        features = np.array(
            [data[feature] for feature in FEATURE_ORDER]
        ).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Return result
        return jsonify({
            "predicted_gold_price": float(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
