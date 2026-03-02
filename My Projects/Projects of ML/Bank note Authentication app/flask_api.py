from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger #This library is used to create a UI

app=Flask(__name__)
Swagger(app) #This creates separate UI for app i.e Flask(__name__)
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

@app.route('/')  ##welcome page
def welcome():
    return "Welcome All"

@app.route('/predict')
def predict_note_authentication():
    """ Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
    """
    variance = float(request.args.get('variance'))
    skewness = float(request.args.get('skewness'))
    curtosis = float(request.args.get('curtosis'))
    entropy = float(request.args.get('entropy'))

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted value is " + str(prediction)



@app.route('/predict_file',methods=["POST"])# we make it post ##another api
def predict_note_file():
    """Let's Authenticate Banks Note
    This is using docstrings for specification
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
    responses:
        200:
            description: The output values
    
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    return str(list(prediction))




if(__name__=='__main__'):
    app.run()
    
    #ps -> the """ xyz   """ is the UI creation request that 
    #we have to make in order to post and get all the required 
    #values in order to predict and show in the frontend.
    