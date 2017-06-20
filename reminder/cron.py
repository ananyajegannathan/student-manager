from memo import settings
from reminder.models import Reminder
from django.contrib.auth.models import User


def job():
	send_mail(Reminder.topic, 'body of the message', 'noreply@parsifal.co', [User.email])


