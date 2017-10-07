from flask import render_template, url_for, redirect, flash
import os
from app import app, forms, sg
from app.forms import EmailForm
import sendgrid
from sendgrid.helpers.mail import *
from validate_email import validate_email


@app.route('/')
def home():
    pictures = [file for file in os.listdir(app.config['PICTURES_LOCATION']) 
                if file.endswith(('.jpeg', '.jpg', '.png'))]
    print('pictures:', pictures)
    descriptions = [os.path.splitext(file)[0] for file 
                in os.listdir(app.config['PICTURES_LOCATION'])
                if file.endswith(('.jpeg', '.jpg', '.png'))]
    print('descriptions:', descriptions)
    return render_template('home.html',
                            picturesdescriptions=zip(pictures, descriptions))

@app.route('/about')
def about():
    return render_template('about.html',
                            title='About Us')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    emailform = EmailForm()


    if emailform.validate_on_submit():
        if not validate_email(emailform.email.data):
            flash('Could not verify email \'' + emailform.email.data + '\'', 'danger')
            return redirect(url_for('contact'))


        #disable emails on localhost to avoid wasting free emails
        if os.environ.get('HEROKU'):
            from_email = Email(app.config['TO_EMAIL'])
            subject = 'Free Quote Request from ' + emailform.email.data
            to_email = Email(app.config['TO_EMAIL'])
            content = Content('text/plain', 'Hello! Someone has requested a free quote on \
                                            onesbsi.com. Here\'s what they said: \n\n\n\n' + 
                                            emailform.body.data + '\n\n' + 'FROM: ' + 
                                            emailform.email.data)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
        else:
            print('Fake email sent')

        flash('We\'ve received your quote request and will get back to you ASAP. Thanks!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html',
                            contactinfo=app.config['CONTACT_INFO'],
                            title='Contact',
                            emailform=emailform)

@app.route('/services')
def services():
    return render_template('services.html',
                            title='Services')