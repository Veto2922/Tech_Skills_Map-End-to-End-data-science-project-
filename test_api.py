# from flask import Flask, request, jsonify
# import joblib
# import pandas as pd
# import json

# skills = ['Python' , 'Scikit-Learn' , 'TensorFlow' , 'NumPy' , 'Pandas' , 'Opencv']


# pred = request.post('http://127.0.0.1:5000/predict' , data = json.dumps( skills ) ,  
#                     headers = {'content-type' : 'application/json'})


# print(pred)


import requests

# API URL
api_url = 'http://127.0.0.1:5000/predict'  # Update with the correct host and port if necessary

# Skills list for testing
skills = ['Python' , 'Scikit-Learn' , 'TensorFlow' , 'NumPy' , 'Pandas' , 'Opencv']

# JSON payload
json_payload = {'skills': skills}

# Send POST request
response = requests.post(api_url, json=json_payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    prediction = result['prediction']
    print(f'Prediction: {prediction}')
else:
    print(f'Error: {response.status_code} - {response.text}')
