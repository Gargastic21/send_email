from flask import Flask,request, render_template
import requests
import json
app = Flask(__name__)

api_url = "https://6w64ss0rbf.execute-api.us-east-1.amazonaws.com/dev"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers = {"Content-Type":"application/json"}


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/form_login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
       if request.form.get('button') == 'click':
           print(request.form.get('button'))
           print("yes")
           requests.post(api_url, headers=headers)
           return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)



