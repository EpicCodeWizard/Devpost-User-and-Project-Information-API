"""
MULTIPLE PAGES:
PROJECTS
HACKATHONS
ACHIEVEMENTS
FOLLOWERS
FOLLOWING
"""

from flask import Flask, jsonify, redirect
from info import user, project
import requests

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def homepath():
  return jsonify({"Usage": "/user/USERNAME to query a user and /project/NAME to query a project"})

@app.route("/user/<username>")
def userpath(username):
  mainreq = requests.get('https://devpost.com/' + username, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'})
  if mainreq.status_code != 404:
    pass
  else:
    return jsonify({"Error": "UserNotFoundError"})
  return jsonify(user(mainreq, username))

@app.route("/project/<name>")
def projectpath(name):
  mainreq = requests.get('https://devpost.com/software/' + name, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'})
  if mainreq.status_code != 404:
    pass
  else:
    return jsonify({"Error": "ProjectNotFoundError"})
  return jsonify(project(mainreq, name))

@app.errorhandler(404)
def page_not_found(e):
  return jsonify({"Error": "PathNotFoundError (usage: /user/USERNAME to query a user and /project/NAME to query a project)"}), 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
