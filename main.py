#Versuch, meine home.html Datei mit der main.py zu verknüpfen, damit die Datei auf meinem Localhost angezeigt wird.

from flask import Flask
from flask import render_template    

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/Jasmin")
def Jasmin():
    return "Hello, Jasmin"
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)

	