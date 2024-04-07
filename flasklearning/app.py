from flask import Flask
app=Flask(__name__)#acts as wsgi 

@app.route('/')
# @app.route('/'): This line is a decorator in Python. Decorators are a way to modify functions or methods. In this case, it modifies the welcome function 
# to indicate that it should be called when the root URL '/' is accessed in the web browser. So, when someone visits the main page of your website (http://yourwebsite.com/), the welcome function will run.
def welcome():
    return "Welcome to first flask hello"
@app.route('/mem')
def jj():
    return "hello everyone"










if __name__=='__main__':
    app.run(debug=True)
    #app.run(debug=True)=>we can change in realtime and no need to run again just save
    #default port is 5000