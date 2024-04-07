from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/result/<int:score>/<name>')
def result(score,name):
    return render_template('result.html',result=score,name=name)
    
@app.route('/submit',methods=['post','get'])
# if this method is called by the form then it should contain the methods option also in the decorator
def submit():
    sum=0
    score=0
    if request.method=='POST':
        name=request.form['name']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        sum=num1+num2
    return redirect(url_for('result',score=sum,name=name))
# score=sum is where you're defining a parameter to be passed to the 'result' endpoint. The important thing to note here is that the name 'score' should match the name that your result() function expects.





if __name__ == '__main__':
    app.run(debug=True)