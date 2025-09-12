from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.get_json()  # odbiera JSON z fetch
        name = data.get("name", "Anonim")
        return jsonify({"message": f"Witaj, {name}!"})
    return render_template("index.html")  # GET → zwraca stronę

if __name__ == "__main__":
    app.run(debug=True)
