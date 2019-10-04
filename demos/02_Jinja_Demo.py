from flask import Flask
from flask import render_template

app = Flask("Hello World")

@app.route('/hello')
def hello_world():
    return render_template('index.html', name="Jasmin")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
#Um Auszuführen wieder auf den Anaconda Reader dings, und dann python und die Datei eingeben.
#Danach wieder auf dem Webbrowser --> localhost:5000\hello 