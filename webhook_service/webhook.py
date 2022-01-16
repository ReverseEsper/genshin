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
    # 1. Update Git Repository
    g = git.cmd.Git("/root/Git/genshin")
    g.pull()
    # 2. If webhook was changed, restart webhook service
    # Test 1
    return 'Webhooks with Python'


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0",port=8081)

