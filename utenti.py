from  flask import Blueprint


utenti_Blueprint=Blueprint("userfun",__name__)


@utenti_Blueprint.route('/profile')
def profiletest():
    return "User Profile Page"
