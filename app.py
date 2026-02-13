from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recipes = []

    if request.method == "POST":
        ingredients = request.form["ingredients"].lower()

        if "egg" in ingredients:
            recipes.append("Egg Omelette")
            recipes.append("Egg Fried Rice")
        if "potato" in ingredients:
            recipes.append("Potato Curry")

    return render_template("index.html", recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)



