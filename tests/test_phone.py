from invoke.services.email import EmailInvoke
from invoke.services.finder import FinderInvoke
from flask import Flask, jsonify

"""
PHONE服务

"""

app = Flask("api_server")

# app.config['F_EMAIL_ADDR'] = "http://127.0.0.1:5000"

app.config['USE_FINDER'] = True
app.config['F_FINDER_ADDR'] = "http://127.0.0.1:1000"

e = EmailInvoke()
# 第一种方式
# e.init_app(app)


# 第二种方式
finder = FinderInvoke()
finder.init_app(app)

if 'USE_FINDER' in app.config:
    e.update_from_finder(finder)


@app.route('/')
def index():
    print(e.get_hello())
    return jsonify(hello="hello world")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
