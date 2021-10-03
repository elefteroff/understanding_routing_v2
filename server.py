from flask import Flask 
app = Flask(__name__)    

@app.route('/') 
def hello():
    return("Hello World!")

@app.route('/dojo') 
def dojo():
    return("Dojo!")

@app.route('/say/<string:name>') 
def hi_name(name):
    return(f"Hi {name}!")

@app.route('/repeat/<int:num>/<string:word>') 
def word_repeat(word,num):
    return(f"{word}" * num)

if __name__=="__main__":
    app.run(debug=True)