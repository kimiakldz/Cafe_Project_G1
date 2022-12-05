from flask import render_template



def menu():

    return render_template('menu.html', title='Menu')