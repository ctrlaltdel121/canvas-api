from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/user_input', methods=['POST'])
def processInput():
    name = request.form.get('name')
    ret = {}
    ret['message'] = "Hello %s" %name
    return jsonify(ret)

app.run(threaded=True)