from flask import Flask
from flask import render_template

app = Flask(__name__)

users = ['alex', 'john', 'bob']

@app.route('/<theme>')
# @app.route('/')
def home(theme = "light"):
    if theme == 'light' or theme == 'dark':
      return render_template('main/content/index.html', theme=theme)
    else:
       return render_template('main/content/index.html', theme='light')


@app.route('/<theme>/news')
def news(theme = "light" and "dark"):
    return render_template('news/content/index.html', theme=theme)


@app.route('/<theme>/profile/<username>')
def show_user_profile(username):
  global users

  if username in users:
    return f'User {username.title()}'
  else:
     return "Пользователь не найден!"


if __name__ == '__main__':
    app.run(debug=True)