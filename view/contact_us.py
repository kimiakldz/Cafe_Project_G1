from flask import render_template


def contact_us():
    return render_template('contact_us.html', title='Contact Us')
