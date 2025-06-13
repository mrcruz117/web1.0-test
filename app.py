from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/contacts")


if __name__ == "__main__":
    # enable auto-reload & debug output
    app.run(debug=True)
