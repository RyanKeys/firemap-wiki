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
    return render_template('documentation.html')

@app.route("/documentation/<selection>")
def read_selection(selection):
    if str(selection).lower() == "coordinates":
        context =  {
            "name": "Coordinates",
            "summary": "Displays the latitude and longitude of selected fire.",
            "description": "Accessible thorugh the Active Fire Map GUI, or by creating an API key and going to the '/api/fires' endpoint.",
        }
    else:
        context = {
            "name": f"{selection}",
            "summary": "pellentesque habitant morbi tristique senectus",
            "description": """tempus quam pellentesque nec nam aliquam sem et tortor consequat id porta nibh venenatis cras sed felis eget velit aliquet sagittis id consectetur purus ut faucibus pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper quis lectus nulla at volutpat diam ut venenatis tellus in metus vulputate eu scelerisque"""
        }
    return render_template('detail.html', context=context)

if __name__ == "__main__":
    app.run()
