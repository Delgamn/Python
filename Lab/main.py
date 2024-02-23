from pathlib import Path
from flask import Flask
from flask import make_response
from flask import send_file
from flask import render_template
import Config

# Creating an instance of the Flask class
app = Flask(__name__)


# The main page of the site
@app.route('/')
def main():
    return render_template('Home.html')


# A non-existent page
@app.route('/<text>')
def error(text):
    return make_response("Page not found", 400)


# Button click processing
@app.route("/Download")
def download(filename='flask.pdf'):
    # Path is used for multiplatform
    safe_path = Path(app.config["UPLOAD_FOLDER"], filename)
    try:
        return send_file(safe_path, mimetype='application/pdf', as_attachment=True)
    except FileNotFoundError:
        # Output a message about the absence of a file
        return make_response("File not found", 404)


if __name__ == '__main__':
    # Downloading settings from a configuration file
    app.config.from_object(Config.BaseConfig)
    app.run()
