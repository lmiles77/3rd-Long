# #import Flask 
# from flask import Flask
# #create an instance of Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return "Hello World"
# if __name__ == '__main__':
#     app.run(debug=True)

import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib 
import sklearn


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

    form_data = request.form.to_dict()
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

def ValuePredictor(data):
    data= np.array(data).reshape(-1, 9)
    return model.predict(data)

if __name__ == '__main__':
    app.run(debug=True)