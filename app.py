#app.py
from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open('rf.pkl','rb'))

@app.route('/',methods=('GET', 'POST'))
def blank(): 
    return redirect(url_for('predict'))

@app.route('/predict/', methods=['POST','GET']) 
def predict():
    if request.method == 'POST':
        V1 = request.form['V1']
        V2 = request.form['V2']
        V3 = request.form['V3']
        V4 = request.form['V4']
        V5 = request.form['V5']
        V6 = request.form['V6']
        V7 = request.form['V7']
        V8 = request.form['V8']
        V9 = request.form['V9']
        x = [[V1, V2, V3, V4, V5, V6, V7, V8, V9]]
        res = int(model.predict(x))
        if (res == 0): pred = 'You will not have chronic kidney Disease '
        else : pred = 'You will have chronic kidney Disease'
        return render_template('index.html', pred=pred )
    return render_template('index.html' )

if __name__ == '__main__':
    app.run(debug=False)
