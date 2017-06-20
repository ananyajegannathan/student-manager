from rest_framework import serializers
from django.contrib.auth.models import User
from reminder.models import UserProfile, List, Item, Subject, Timetable, Attendance
from django.core.exceptions import ValidationError

class UserProfileSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source = 'user.username')
	password = serializers.CharField(source = 'user.password')
	email = serializers.EmailField(source = 'user.email')
	first_name = serializers.CharField(source = 'user.first_name')
	last_name = serializers.CharField(source = 'user.last_name')
	lists = serializers.HyperlinkedRelatedField(view_name='list-detail', many=True, read_only=True)
	
	class Meta:
		model = UserProfile
		fields = ('first_name','last_name','username','gender','phone_no','email','password','lists')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user = User.objects.create_user(**user_data)
		password = user_data.pop('password', None)
		pwd = User()
		if password is not None:
			pwd.set_password(password)
		pwd.save()
		profile = UserProfile.objects.create(user=user, **validated_data)
		return profile

	def update(self, instance, validated_data):
		user_data = validated_data.pop('user', None)
		for attr, value in user_data.items():
			if attr == 'password':
				instance.user.set_password(value)
			else:
				setattr(instance.user, attr, value)
		# Then, update UserProfile
		for attr, value in validated_data.items():
			setattr(instance, attr, value)
		instance.save()
		return instance

class ListSerializer(serializers.HyperlinkedModelSerializer):
	items = serializers.StringRelatedField(many=True, read_only=True)

	class Meta:
		model = List
		fields = ('url','id','title', 'items')

class ItemSerializer(serializers.ModelSerializer):

	class Meta:
		model = Item
		fields = ('item_list','item','item_date','is_completed','set_reminder','time','extra_notes')

# class PrimaryKeyNestedMixin(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):

#     def to_internal_value(self, data):
#         return serializers.PrimaryKeyRelatedField.to_internal_value(self, data)

#     def to_representation(self, data):
#         return serializers.ModelSerializer.to_representation(self, data)

class SubjectSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = ('name',)

class TimetableSerializer(serializers.HyperlinkedModelSerializer):
	subjects = SubjectSerializer(many=True, queryset=Subject.objects.all())

	class Meta:
		model = Timetable
		fields = ('url','day','subjects')

class AttendanceSerializer(serializers.ModelSerializer):
	current_percent = serializers.SerializerMethodField()
	subject = SubjectSerializer(queryset=Subject.objects.all())

	class Meta:
		model = Attendance
		fields = ('reqd_percent','subject','conducted','attended','current_percent')

	def get_current_percent(self):
		result = (self.attended/self.conducted)*100
		return result
