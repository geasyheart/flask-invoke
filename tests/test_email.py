from flask import Flask, jsonify

from invoke.services.phone import PhoneInvoke

app = Flask(__name__)

"""

EMAIL 服务
"""

# app.config['F_PHONE_ADDR'] = "http://127.0.0.1:8080"
#
# phone = PhoneInvoke()
# phone.init_app(app)


@app.route('/')
def index():
    # print(phone.get_index())
    return "index"


@app.route('/get')
def get_get():
    return jsonify(hello="world")


if __name__ == "__main__":
    app.run(port=5000)
