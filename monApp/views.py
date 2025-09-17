from .app import app
from flask import render_template

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html", title="R3.01 Dev Web avec Flask", name="Cricri"
    )

@app.route('/about/')
def about():
    return render_template("about.html", title="À propos")

@app.route('/contact/')
def contact():
    return render_template("contact.html", title="Contact", numero="07 23 34 31 28")

if __name__ == "__main__":
    app.run()