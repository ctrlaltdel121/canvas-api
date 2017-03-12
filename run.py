from flask import Flask, request, send_from_directory, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index2.html')

@app.route('/user_input', methods=['POST'])
def processInput():
    name = request.form.get('name')
    ret = {}
    ret['message'] = subprocess.check_output(["./runner", name])
    return jsonify(ret)

app.run(host="0.0.0.0", port=os.environ['PORT'], threaded=True)
