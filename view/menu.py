from flask import render_template
from core.manager import db
from models.menuitem import Menu


def menu():
    items = db.session.execute(db.select(Menu)).scalars().all()
    return render_template('menu.html', title='Menu', items=items)
