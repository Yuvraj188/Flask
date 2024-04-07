# integrate html with flask
# http verb GET and POST
from flask import Flask, redirect,url_for,render_template,request
#for redirect create folder name template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res="fail"

    return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person failed has marks is " + str(score)

@app.route('/results/<int:score>')
def resu(score):
    result = ''
    if score < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=score))
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
   
    return redirect(url_for(success,score=total_score))
#name will be passed in this    request.form['name']

if __name__ == '__main__':
    app.run(debug=True)
