import datetime
import schedule
import time
from reminder.models import Reminder
from django.contrib.auth.models import User
from django.core.mail import send_mail


class SendEmail(Reminder):

	def job(self):
		send_mail(Reminder.topic, 'body of the message', 'noreply@parsifal.co', [User.email])

	def send(self):
		time = str(Reminder.time)

		if self.freq == Reminder.once:
			if self.reminder_date == datetime.datetime.now().date() && self.time == datetime.datetime.now().time():
				job()
		elif self.freq == Reminder.daily:
			schedule.every().day.at(time[0:5]).do(job)
		elif self.freq == Reminder.weekly:
			if self.day_of_week == 0:
				schedule.every().sunday.at(time[0:5]).do(job)
			elif self.day_of_week == 1:
				schedule.every().monday.at(time[0:5]).do(job)
			elif self.day_of_week == 2:
				schedule.every().tuesday.at(time[0:5]).do(job)
			elif self.day_of_week == 3:
				schedule.every().wednesday.at(time[0:5]).do(job)
			elif self.day_of_week == 4:
				schedule.every().thursday.at(time[0:5]).do(job)
			elif self.day_of_week == 5:
				schedule.every().friday.at(time[0:5]).do(job)
			else:
				schedule.every().saturday.at(time[0:5]).do(job)
		elif self.freq == Reminder.monthly:
			schedule.every(4).weeks.at(time[0:5]).do(job)
		else:
			schedule.every(52).weeks.at(time[0:5]).do(job)





