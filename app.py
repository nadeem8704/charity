from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for sessions

# Home Page - Professional and colorful
@app.route("/")
def home():
    return render_template("index.html")

# Join Us Page - For account creation, login, and donation options
@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        # Here you can later add processing for creating an account or logging in
        # For now, we'll simply redirect to home
        return redirect(url_for("home"))
    return render_template("join.html")

# About Us Page - Description about the charity
@app.route("/about")
def about():
    return render_template("about.html")

# Example Login route - Processes login requests from join page
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    # Insert your login validation logic here (this is just a demo)
    session["user"] = username
    resp = make_response(redirect(url_for("home")))
    # Set a demo cookie for demonstration purposes
    resp.set_cookie("user_type", "donor")
    return resp

# Dummy Donate route for demonstration
@app.route("/donate")
def donate():
    return "Donate page - under construction!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
