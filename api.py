from flask import Flask, request, jsonify
import joblib
import pandas as pd
from src.models.predict_model import PredictPipeline , DataDetails

# Create Flask App
app = Flask(__name__)


# Create API routing call
@app.route('/predict', methods=['POST'])
def predict():
    
    # Get JSON Request
    skills_list = request.get_json()
    # Convert JSON request to Pandas DataFrame
    print('skills list ===============' , skills_list['skills'])
    # Get prediction
    model = PredictPipeline(skills_list['skills'])
    pred = model.prediction_prob()
    # Return JSON version of Prediction
    return jsonify({'prediction': str(pred)})

        

if __name__ == '__main__':


    app.run(debug=True)