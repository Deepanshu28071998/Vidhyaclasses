from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home_page.html")

@app.route("/about")
def about():
    return render_template("About_us.html")

@app.route("/contact")
def contact():
    return render_template("Contact_Us.html")

@app.route("/courses")
def courses():
    return render_template("Courses.html")

@app.route("/youtube")
def youtube():
    return render_template("Youtube.html")


app.run(debug = True)