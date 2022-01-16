from flask import Flask,request,json
from flask_cors import CORS

from pprint import pprint as pp
import git

from subprocess import call

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
    g = git.cmd.Git("/root/Git/genshin")
    g.pull()
    # Check if webhook was modified
    if "commits" in data:
        for commit in data["commits"]:
            if commit['modified']:
                print(f"Modified File: {commit['modified']}")
                if 'webhook_service/webhook.py' in commit['modified']:
                    print ("Webhook modified, has to restart service")
                    # So... now we have to ... restart that service ? 
                    
                    call(["systemctl", "daemon-reload"])
                    call(["systemctl", "restart webhook.service"])
                    print("Service Restarted")
            
        
    return 'Webhooks with Python'


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0",port=8081)

#Test Commit 3

