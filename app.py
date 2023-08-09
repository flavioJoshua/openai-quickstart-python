import os

import openai
from flask import Flask, redirect, render_template, request, url_for,session
from utenti  import utenti_Blueprint
from test_post_btn  import post_Blueprint




app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
app.secret_key="oooo difficilissima "

""" register  del bluePrint"""
app.register_blueprint(utenti_Blueprint,url_prefix="/profilo" )
app.register_blueprint(post_Blueprint,url_prefix="/post_btn")





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


@app.route('/seconda_pagina_url', methods=['GET', 'POST'])
def seconda_pagina():
    if request.method == 'GET':
        print('seconda pagina Get')
        return render_template('seconda.html')
    elif request.method == 'POST':
        _args = request.args
        print("seconda pagina Post :", _args)
        return redirect(url_for('seconda_pagina'), **_args)