from flask import Flask
from flask import render_template
import os
import time
import asyncio
import htmlc as hc

app = Flask(__name__)

users = ['alex', 'john', 'bob']

@app.route('/<theme>')
def home(theme = "light"):
    if theme == 'light' or theme == 'dark':
      return render_template('main/content/index.html', theme=theme)
    else:
      return render_template('main/content/index.html', theme='light')


@app.route('/<theme>/news')
def news(theme = "light" and "dark"):
    if theme == 'light' or theme == 'dark':
      return render_template('news/content/index.html', theme=theme)
    else:
      return render_template('news/content/index.html', theme='light')

@app.route('/<theme>/news.<news>')
def news_content(news :str, theme = 'light'):
  try:
    return render_template(f'news/content/news/{news}.html', theme=theme, news=news)
  except:
    return render_template('news/error404.html')

@app.route('/<theme>/profile/<username>')
def show_user_profile(username):
  global users

  if username in users:
    return f'User {username.title()}'
  else:
    return "Пользователь не найден!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
