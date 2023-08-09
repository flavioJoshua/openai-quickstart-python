from  flask import Blueprint
from flask import Flask, redirect, render_template, request, url_for,session



post_Blueprint=Blueprint("test_post",__name__)


@post_Blueprint.route('/execute_function', methods=['POST','GET'])
def execute_function():
    # Qui puoi inserire il codice che vuoi eseguire lato server
    print("Funzione eseguita lato server!")
    return redirect(url_for('index'))