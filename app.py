from flask import Flask, render_template, request

from calculator import quadratic


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        a = request.form["a"]
        result = 'Shaun'

        if root_1:
            return render_template(
                "calculator_result.html", a=a, result = result
            )
        else:
            return render_template("calculator_form.html", error=True)
    return render_template("calculator_form.html", error=None)
