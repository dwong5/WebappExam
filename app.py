from flask import Flask, render_template, request

from calculator import *


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        a = str(request.form["a"])
        gender = str(request.form["gender"])
        result = same_value(a)
        result1 = highest_year(a,gender)

        if a:
            return render_template(
                "calculator_result.html", a=a, gender = gender, result = result, result1 = result1
            )
        else:
            return render_template("calculator_form.html", error=True)
    return render_template("calculator_form.html", error=None)
