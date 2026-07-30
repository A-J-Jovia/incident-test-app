import requests
import json
from datetime import datetime

# Removed import punycode as it's deprecated and caused the deprecation warning

def get_repositories(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_repository_content(owner, repo, path):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    url = "https://api.github.com/repos/octocat/Hello-World"
    repositories = get_repositories(url)
    
    if repositories:
        owner = repositories["owner"]["login"]
        repo = repositories["repo"]["name"]
        path = "main.py"
        content = get_repository_content(owner, repo, path)
        
        if content:
            filename = "main.py"
            print(json.dumps(content, indent=4))
            print("File Name:", filename)

if __name__ == "__main__":
    main()