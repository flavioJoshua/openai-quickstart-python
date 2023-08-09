import os

import openai
from flask import Flask, redirect, render_template, request, url_for,session
from utenti  import utenti_Blueprint




app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
app.secret_key="oooo difficilissima "

""" register  del bluePrint"""
app.register_blueprint(utenti_Blueprint,url_prefix="/profilo" )




@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    
    return render_template("index.html",_valore="qualcosa da  scrivere" ,result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )


@app.route('/seconda_pagina' )
def seconda_pagina():
    return render_template('seconda.html')


#TODO  test  di  funzionamento
