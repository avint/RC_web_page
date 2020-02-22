from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)
a=[1,2,3,'afsf']



@app.route('/')
def f1():
    return render_template('index.html',n=a)

@app.route('/new', methods=['POST'])
def num():
    a.append(request.form.get('num'))
    return render_template('index.html',n=a)
if __name__=='__main__':
    app.run(debug=True)