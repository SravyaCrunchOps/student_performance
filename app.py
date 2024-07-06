import os
import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# start flask app
app = Flask(__name__)

# Cors
CORS(app)

# load the model and scaler
if os.path.isfile("D:/machine learning/basics/my_linear_model.pkl"):
    with open("D:/machine learning/basics/my_linear_model.pkl", "rb") as f:
        model_lr, scaler = pickle.load(f)
else:
    raise FileNotFoundError

# data pre-processing

# home page
@app.route('/')
def index():
    return render_template('index.html')

# predict route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    # conver req.data to dataframe
    X_new = pd.DataFrame([data])

    print(X_new)

    # pre-process 'extra-curricular activity' 
    X_new['Extracurricular Activities'] = X_new['Extracurricular Activities'].map({'No': 0, 'Yes': 1})

    # standardize the dataset values into single unit
    X_new_scaled = scaler.transform(X_new)

    # predict the outcome
    y_pred_new = model_lr.predict(X_new_scaled)
    print(y_pred_new[0])

    return jsonify({'prediction': round(y_pred_new[0], 2)})


if __name__ == '__main__':
    app.run(debug=True)