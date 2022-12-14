import os
# import mysql.connector
# from mysql.connector import Error
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.debug = True    
app.run()
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        mypromt = request.form["prompt"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=mypromt,
            temperature=0.6,
            max_tokens=4000
        )
        return redirect(url_for("index", result=response.choices[0].text))
    result = request.args.get("result")
    return render_template("index.html", result=result)

