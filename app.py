
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib 
from sklearn.preprocessing import LabelEncoder


#prediction
app = Flask(__name__)
model = joblib.load('classifier.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/', methods=['POST'])
def ValuePredictor():
    print(request.form)
    
    ToGo = request.form["togo"] 
    Formation_NOHUDDLE = 0
    Formation_NOHUDDLESHOTGUN = 0 
    Formation_SHOTGUN = 0
    Formation_UNDERCENTER = 0 
    PlayType_PASS = 0
    PlayType_RUSH = 0
    PlayType_SACK = 0
    PlayType_SCRAMBLE = 0   

    if request.form["formation"] == "no huddle":
        Formation_NOHUDDLE = 1
    elif request.form["formation"] == "no huddle shotgun":
        Formation_NOHUDDLESHOTGUN = 1
    elif request.form["formation"] == "shotgun":
        Formation_SHOTGUN = 1
    elif request.form["formation"] == "under center":
        Formation_UNDERCENTER = 1
    elif request.form["play"] == "pass":
        PlayType_PASS = 1
    elif request.form["play"] == "rush":
        PlayType_RUSH = 1
    elif request.form["play"] == "sack":
        PlayType_SACK = 1
    elif request.form["play"] == "scramble":
        PlayType_SCRAMBLE = 1
    
    form_data =[
        Formation_NOHUDDLE,
        Formation_NOHUDDLESHOTGUN, 
        Formation_SHOTGUN,
        Formation_UNDERCENTER, 
        PlayType_PASS,
        PlayType_RUSH,
        PlayType_SACK,
        PlayType_SCRAMBLE        
    ]
    # convert form_data into a form like [2,0,0,1,0,0,1,0,0]
    form_data= list(form_data.values())
    form_data = list(map(int, form_data))
    result = ValuePredictor(form_data)
    
    if int(result) == 1:
        prediction = 'YOU DID IT! CONVERSION SUCCESSFUL, VICTORY DANCE IS ON POINT!'
    else:
        prediction = 'You need more practice, better luck next time.'
    print (prediction)
    return prediction 

def VVP(data):
    data= np.array(data).reshape(-1, 9)
    return model.predict(data)

if __name__ == '__main__':
    app.run(debug=True)

# from flask import (Flask, render_template, request)
# import pandas as pd
# import numpy as np
# import joblib

# app = Flask(__name__)
# model = joblib.load(open("classifier.pkl", "rb"))
# # prediction function


# @app.route('/')
# def home():
#     return render_template('index.html')


# # @app.route('/page2')
# # def page2():
# #     return render_template('index2.html')


# @app.route('/predict', methods=['POST'])
# def ValuePredictor(to_predict_list):
#     to_predict = np.array(to_predict_list).reshape(1, 8)
#     result = model.predict(to_predict)
#     return result[0]


# @app.route('/result', methods=['POST'])
# def result():
#     if request.method == 'POST':
#         to_predict_list = request.form.to_dict()
#         to_predict_list = list(to_predict_list.values())
#         to_predict_list = list(map(int, to_predict_list))
#         result = ValuePredictor(to_predict_list)
#         if int(result) == 1:
#             prediction = 'YOU DID IT! CONVERSION SUCCESSFUL, VICTORY DANCE IS ON POINT!'
#         else:
#             prediction = 'You need more practice, better luck next time.'
#         return prediction


# if __name__ == '__main__':
#     app.run(debug=True)
