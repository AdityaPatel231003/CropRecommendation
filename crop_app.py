from flask import Flask,request,render_template
import numpy as np
import pandas 
import pickle
import sklearn


#import moodel
model=pickle.load(open('model.pkl','rb'))

#creating flask app
app= Flask(__name__)



@app.route('/')
def home():
    return render_template("home.html")


@app.route('/Predict')
def prediction():
    return render_template('index.html')

@app.route("/GET",methods=['POST'])
def predict():
    N = float(request.form['Nitrogen'])
    P =float(request.form['Phosporus']) 
    K = float(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph =float(request.form['Ph']) 
    rainfall = float(request.form['Rainfall'])

    values= [N, P, K, temp, humidity, ph, rainfall]
   
    single_pred = np.array(values).reshape(1, -1)
    prediction = model.predict(single_pred)


      

    if ph>0 and temp<=100 and humidity>0:
        result = prediction[0]
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    return render_template('index.html',result = result)




#python main
if __name__=='__main__' :
    app.run(debug=True)
    















