import flask

app = flask.Flask(__name__) 

@app.route("/")
def home():
	return flask.render_template("home.html")

@app.route("/ESC")
def routeESC():
	return flask.render_template("ESC-Select.html")

@app.route("/NFs")
def routeNF():
	return flask.render_template("NF-Select.html")

@app.route("/Other")
def routeOther():
	return flask.render_template("Other-Select.html")

@app.route("/Ideal")
def routeIdeal():
	return flask.render_template("Ideal-Select.html")

if __name__ == "__main__":
	app.run() 