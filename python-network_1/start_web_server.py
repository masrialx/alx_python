from flask import Flask, Response

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    res = Response("This is a test response.")
    res.headers["X-Request-Id"] = "School"
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
