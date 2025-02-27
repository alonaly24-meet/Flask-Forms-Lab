from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

username = "llo2ay"
password = "123"
facebook_friends=["malak","rut","nada", "talyah", "and more"]

alowed_accounts={"llo2ay":"123","alona":"alona","sam":"999"}

@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method=="POST":
		if username in alowed_accounts and username==request.form.get("username").lower() and password==request.form.get("password"):
			return redirect(url_for('home'))
		else:
			return render_template("login.html")
	else:  
		return render_template('login.html')

@app.route("/home",methods=["GET","POST"])
def home():
	return render_template('home.html',friends=facebook_friends)

@app.route('/friend_exists/<string:friend_name>', methods=['GET', 'POST'])
def friend_exists(friend_name):
    return render_template('friend_exists.html', friend_name=friend_name, friends=facebook_friends)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)