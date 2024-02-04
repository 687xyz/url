from flask import Flask, redirect, url_for
import json

app = Flask(__name__)

# 加载链接
def load_links():
    with open('links.json') as f:
        return json.load(f)

@app.route('/')
def home():
    return '首页'

@app.route('/<name>')
def goto_link(name):
    links = load_links()
    if name in links:
        return redirect(links[name])
    else:
        return process.env.PAGEERR, 404

if __name__ == '__main__':
    app.run(debug=True)
