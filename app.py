from flask import Flask, render_template
from flask import request
from markdown import markdown
import requests
import os

app = Flask(__name__)

PASSWORD = os.environ.get('PASSWORD')

@app.template_filter('markdown')
def render_markdown(text):
    return markdown(text)

#  ДОМАШНЯЯ
@app.route('/')
@app.route('/<theme>/')
@app.route('/<theme>')
def home(theme="light"):
    if theme in ['light', 'dark']:
        return render_template('main/content/index.html', theme=theme)
    return render_template('main/content/index.html', theme='light')

#  НОВОСТИ
@app.route('/<theme>/news/')
@app.route('/<theme>/news')
def news(theme="light"):
    if theme in ['light', 'dark']:
        return render_template('news/content/index.html', theme=theme)
    return render_template('news/content/index.html', theme='light')

#  НОВОСТЬ
@app.route('/<theme>/news.<news>')
def news_content(news: str, theme='light'):
    try:
      fl = open(f'mdnews/{news}.md', 'r', encoding='utf-8')
      fl = f"{fl.read()}"
    except:
      return render_template('/news/error404.html', theme=theme)
    
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
    return render_template('markdown.html', content=response.text, theme=theme, news=news)

@app.route("/<theme>/adpan", methods=['GET', 'POST'])
def adpan(theme):
    if request.method == 'POST':
        password = request.form['password']
        if password == PASSWORD:
            return render_template("/adpan/adpan.html", theme=theme)
    return render_template("/adpan/main.html", theme=theme)

#  АККАУНТЫ FUNCOFF
# @app.route('/<theme>/profile/<username>')
# def show_user_profile(username):
#     if username in users:
#         return f'User {username.title()}'
#     return "Пользователь не найден!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Используем PORT из переменной окружения или 5000 по умолчанию
    app.run(host='0.0.0.0', port=port)
