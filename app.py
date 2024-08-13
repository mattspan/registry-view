import os
from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

DOCKER_REGISTRY_URL = os.getenv("DOCKER_REGISTRY_URL", "http://localhost:5000/v2")

@app.route('/')
def index():
    repositories = get_repositories()
    return render_template('index.html', repositories=repositories)

def get_repositories():
    response = requests.get(f"{DOCKER_REGISTRY_URL}/_catalog")
    if response.status_code == 200:
        repos = response.json().get("repositories", [])
        return [{ "name": repo, "tags": get_tags(repo) } for repo in repos]
    return []

def get_tags(repo_name):
    response = requests.get(f"{DOCKER_REGISTRY_URL}/{repo_name}/tags/list")
    if response.status_code == 200:
        return response.json().get("tags", [])
    return []

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
