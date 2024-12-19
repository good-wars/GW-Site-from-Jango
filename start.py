import requests
import os

fl = open('mdnews/a.md', 'r', encoding='utf-8')
fl = f"{fl.read()}"

url = "https://api.github.com/markdown"
headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": "547570f885e89c45f6e50c16854f91303fb6fea6"
}
data = {
    "text": fl,
    "mode": "gfm"
}

response = requests.post(url, json=data, headers=headers)
