from flask import *
import os,sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)

user_id = 'admin'
user_pwd = 'admin123'

@app.route('/')
def log():
    return render_template('login.html')

@app.route('/submit_log',methods=['GET','POST'])
def log_sub():
    if request.method=='POST':
        uid = request.form['uid']
        upwd = request.form['pwd']
        error = 'Invalid Credentials'

        if uid == user_id and upwd == user_pwd:
            return render_template('index.html')
        else:
            return render_template('login.html',error=error)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/eda')
def eda():
    return render_template('eda.html')

@app.route('/detector')
def detector():
    return render_template('detector.html')

@app.route('/model_parameter')
def model_parameter():
    return render_template('model_parameter.html')

# @app.route('/display/<filename>')
# def display_image(filename):
#     # print('display_image filename: ' + filename)
#     return redirect(url_for('static', filename='uploads/' + filename))

@app.route('/submit_detector', methods=['POST'])
def choose_file():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import joblib

    import warnings
    warnings.filterwarnings('ignore')

    model = joblib.load('assets/stacked_model.pkl')

# Create an empty dictionary to store user inputs
    user_inputs = {}
    if request.method == 'POST':
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        chestpain = int(request.form['chestpain'])
        restingBP = int(request.form['restingBP'])
        serumcholestrol = int(request.form['serumcholestrol'])
        fastingbloodsugar = int(request.form['fastingbloodsugar'])
        restingrelectro = int(request.form['restingrelectro'])
        maxheartrate = int(request.form['maxheartrate'])
        exerciseangia = int(request.form['exerciseangia'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        noofmajorvessels = int(request.form['noofmajorvessels'])

        # Combine inputs into a single list
        new_user_input = [[age, gender, chestpain, restingBP, serumcholestrol,
                           fastingbloodsugar, restingrelectro, maxheartrate,
                           exerciseangia, oldpeak, slope, noofmajorvessels]]

        # print(new_user_input)
        scaler = joblib.load('assets/scaler.pkl')

        new_user_input_scaled = scaler.transform(new_user_input)

        new_user_output = model.predict(new_user_input_scaled)[0]
        if new_user_output == 0:
            op = "No Heart Disease"
        if new_user_output == 1:
            op = "Risk of Heart Disease Found"
        # print(new_user_output)
        return render_template('detector.html',output=op)



if __name__=='__main__':
    app.run(debug=True)