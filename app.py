from flask import Flask, send_file

app = Flask(__name__)

@app.route("/data", methods=["GET"])
def get_json():
    return send_file("data.json", mimetype="application/json")
