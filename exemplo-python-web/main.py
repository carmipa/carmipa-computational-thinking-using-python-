from flask import Flask, render_template

# explica para flask que a paste tem que ter nome

app = Flask(__name__, static_url_path='static')


@app.route("/")

def home():
    return render_template("templates/index.html")

if __name__=="__main__":
    app.run(debug=True)