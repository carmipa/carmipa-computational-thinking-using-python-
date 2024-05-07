from flask import Flask, render_template

# explica para flask que a paste tem que ter nome

<<<<<<< HEAD
app = Flask(__name__, static_url_path='/static')
=======
app = Flask(__name__, static_url_path='static')
>>>>>>> a29db4ac806bb02956ca2bbe39fd0dd3debb1d99


@app.route("/")

def home():
<<<<<<< HEAD
    return render_template("index.html")
=======
    return render_template("templates/index.html")
>>>>>>> a29db4ac806bb02956ca2bbe39fd0dd3debb1d99

if __name__=="__main__":
    app.run(debug=True)