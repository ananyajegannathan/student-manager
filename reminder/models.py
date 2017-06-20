from django.db import models
from django.core.validators import MaxValueValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class UserProfile(models.Model):
	GENDERS = ((1, 'Male'),
			   (2, 'Female'))
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='profile')
	gender = models.CharField(choices = GENDERS, default = 2, max_length = 64)
	phone_no = models.BigIntegerField()

	def __unicode__(self):
		return self.user.username

	@receiver(post_save, sender = User)
	def create_profile_for_user(sender, instance = None, created = False, **kwargs):
		if created:
			UserProfile.objects.get_or_create(user = instance)

@receiver(post_save, sender=UserProfile)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)

class List(models.Model):
	title = models.CharField(max_length=30)
	user = models.ForeignKey('auth.User', related_name='lists', on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Item(models.Model):
	item = models.CharField(max_length = 50)
	item_date = models.DateField(null=True, blank=True)
	is_completed = models.BooleanField(default=False)
	item_list = models.ForeignKey('List', related_name='items', on_delete=models.CASCADE)
	set_reminder = models.BooleanField(default=False)
	time = models.TimeField('Time to send reminder', blank=True, null=True)
	extra_notes = models.CharField(max_length=500, blank=True, null=True)

	def __str__(self):
		return self.item

class Subject(models.Model):
	name = models.CharField('Subject', max_length=30, default='Subject')
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
 

	def __str__(self):
		return self.name

class Timetable(models.Model):
	day = models.CharField(max_length=3, choices=(	('sun', 'Sunday'),
												  	('mon', 'Monday'),
													('tue', 'Tuesday'),
													('wed', 'Wednesday'),
													('thu', 'Thursday'),
													('fri', 'Friday'),
													('sat', 'Saturday'),
												))
	subjects = models.ManyToManyField(Subject, related_name='subjects')
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


	def __str__(self):
		return self.day
	

class Attendance(models.Model):
	reqd_percent = models.IntegerField('Required Percentage', validators=[MaxValueValidator(100)])
	subject = models.OneToOneField(Subject, related_name='subject')
	conducted = models.IntegerField(default=0)
	attended = models.IntegerField(default=0)
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)