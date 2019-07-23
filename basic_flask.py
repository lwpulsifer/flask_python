from flask import Flask
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    return "<p> Hello! </p>"

if __name__ == "__main__":
    app.run(ssl_context='adhoc')