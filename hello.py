from flask import Flask,request,json
from flask_cors import CORS

from pprint import pprint as pp

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Webhooks with Python'

@app.route('/githubIssue',methods=['POST'])
def githubIssue():
    data = request.json
#    print(f'Issue {data["issue"]["title"]} {data["action"]}')
#    print(f'{data["issue"]["body"]}')
#    print(f'{data["issue"]["url"]}')
    pp (data)
    return 'Webhooks with Python'


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0",port=8081)

