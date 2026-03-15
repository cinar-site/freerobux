from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("l-index.html")

@app.route("/dogrulamasayfasi")
def dogrulama():
    return render_template("l-dogrulamasayfasi.html")

if __name__ == "__main__":
    app.run()
