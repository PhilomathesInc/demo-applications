"""
Minimal application for demo.
"""
from flask import Flask, make_response

app = Flask(__name__)

@app.route("/errorz")
def errorz():
    """
    Handle the /errorz route, return 500 HTTP Status Code.
    """
    return "Something broke!", 500

@app.route("/healthz")
def healthz():
    """
    Handle the /healthz route, return 200 HTTP Status Code and a JSON response
    """
    response = make_response('{"status":"ok"}')
    response.mimetype = 'application/json'
    return response
