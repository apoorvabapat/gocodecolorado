from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps

app = Flask(__name__)
GoogleMaps(app)


@app.route("/")
def hello():
	return render_template("test.html")


if __name__ == "__main__":
	app.run()