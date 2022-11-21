from flask import render_template
from view.form import ContactForm


def contact_us():
    form = ContactForm()
    return render_template('contact_us.html', form=form, title='Contact Us')
    # return render_template('contact_us.html', title='Contact Us')
