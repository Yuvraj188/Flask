# buiilding url dynamically
# variable rules and url building
from flask import Flask,redirect,url_for
#redirect will be used to redirect to other success page
app=Flask(__name__)
@app.route('/')
def welcome():
    return "welcome"

# variable rules and building dynnamically
@app.route('/success/<int:score>')#we have tell it is int otherwise default string

def success(score):
    return "the person has marks is and passed"+ str(score)


@app.route('/success/<int:score>')#we have tell it is int otherwise default string
def fail(score):
    return "the person failed has marks is"+ str(score)
@app.route('/results/<int:score>')

def resu(score):
        result=''
        if score<50:
             result='fail'
            
        else:
             result='success'
        return redirect(url_for(result,score=score ))
#here result is a url which contain fail or success according to situation and call that page named fail and success which we made above 
            
if __name__=='__main__':
    app.run(debug=True)