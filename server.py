from flask import Flask, request
import hashlib
import json
app = Flask(__name__)
@app.route('/')
def index():
    dat="Please run ip:port/hash and send valid json input to get its sha256 hash. Input and Output pattern is \nINPUT : {\"data\":<value to be encoded>}\nOUTPUT : {\"hash\":<sha256 of input>}"
    return dat

@app.route('/hash', methods=['POST'])
def sha256hash():
    req_data = request.get_json()
    inp = req_data['data']
    inter = hashlib.sha256(inp.encode()).hexdigest()
    var = {"hash":""}
    var["hash"] = inter
    hash = json.dumps(var)
    return hash
app.run(debug=False, port=8787)
