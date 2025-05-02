from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about", methods =["GET"])
def about():
    return render_template("index.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"Name: {name}, Email: {email}, Message: {message}")
    return render_template("form.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return f'Name: {name}, Email: {email}'
    return render_template("form.html")

@app.route("/items", methods=["GET"])
def items():
    items = ["Item 1", "Item 2", "Item 3"]
    return jsonify(items)



if __name__ == "__main__":
    app.run(debug=True)