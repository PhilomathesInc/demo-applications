from flask import Flask, make_response

app = Flask(__name__)

@app.route("/errorz")
def errorz():
	return "Something broke!", 500

@app.route("/healthz")
def healthz():
    r = make_response('{"status":"ok"}')
    r.mimetype = 'application/json'
    return r
