
from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("lg.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome to Iris App"

@app.route('/predict',methods=["Get"])
def predict():
    
    """Let's predict the species of Iris flowers:[ 0: 'setosa',1: 'versicolor', 2: 'virginica' ] 
  Using Logistic Regression
 
    ---
    parameters:  
      - name: sepal_length
        in: query
        type: number
        required: true
      - name: sepal_width
        in: query
        type: number
        required: true
      - name: petal_length
        in: query
        type: number
        required: true
      - name: petal_width
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    
    sepal_length=request.args.get("sepal_length")
    sepal_width=request.args.get("sepal_width")
    petal_length=request.args.get("petal_length")
    petal_width=request.args.get("petal_width")

    input_data=np.array([[sepal_length, sepal_width, petal_length, petal_width]], dtype=np.double)
    #prediction=classifier.predict(input_data)
    label_dict = {0:'setosa', 1:'versicolor',2:'virginica'}
    prediction=label_dict[int(classifier.predict(input_data))]

    return "The predicted specie of iris flower is: "+prediction

if __name__=='__main__':
    app.run(host="0.0.0.0", port=3000,debug=True)
  