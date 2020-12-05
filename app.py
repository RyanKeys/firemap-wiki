from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about-us")
def about_us():
    return render_template("about-us.html")

@app.route("/getting-started")
def getting_started():
    return render_template("getting-started.html")

@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

if __name__ == "__main__":
    app.run()
