import os

#for wtforms
WTF_CSRF_ENABLED = True
SECRET_KEY = 'super secret key'

#development only; disables browser caching
if os.environ.get('HEROKU') is None:
    SEND_FILE_MAX_AGE_DEFAULT = 0

#contact information for /contact
CONTACT_INFO = {
	'sanfrancisco': {
		'phone' : '###',
		'email' : '@@@'
	},
	'santa clara' : {
		'phone' : '###',
		'email' : '@@@'
	}
}

#location of pictures
PICTURES_LOCATION = 'app/static/slideshowimages/'

#emails to send quote requests from
FROM_EMAILS = ['@@@']

#emails to send quote requests to
TO_EMAIL = '@@@'

#email w sendgrid
if os.environ.get('HEROKU'):
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME')
    SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
else:
    SENDGRID_API_KEY = 'super secret api key'
    SENDGRID_USERNAME = 'super secret username'
    SENDGRID_PASSWORD = 'super secret password'