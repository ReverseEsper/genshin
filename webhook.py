from flask import Flask,request,json
from flask_cors import CORS

from pprint import pprint as pp
import git

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Webhooks with Python'

@app.route('/githubIssue',methods=['POST'])
def githubIssue():
    data = request.json
    ##pp (data)
    print ("Wydaje mi się, ze jest coś do pociągnięcia")
    g = git.cmd.Git("./")
    g.pull()

    return 'Webhooks with Python'


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0",port=8081)

