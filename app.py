from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

if __name__ == "__main__":
    # enable auto-reload & debug output
    app.run(debug=True)
