from django.shortcuts import render
from rest_framework import viewsets, generics, status, permissions
from django.contrib.auth.models import User
from reminder.models import UserProfile, List, Item, Subject, Timetable, Attendance
from reminder.serializers import (UserProfileSerializer, ListSerializer,ItemSerializer, 
								  SubjectSerializer, TimetableSerializer, AttendanceSerializer)
from rest_framework.decorators import api_view, list_route
from rest_framework.response import Response
from reminder.permissions import IsOwner, UserPermissionsAll, UserPermissionsObj, UserNoPermissions

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes=(UserPermissionsObj,)
	
class UserCreate(generics.CreateAPIView):
	serializer_class = UserProfileSerializer
	permission_classes = (UserNoPermissions,)

class ListViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		return self.request.user.lists.all()
	serializer_class = ListSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class SubjectViewSet(viewsets.ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	permission_classes = (IsOwner,)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class TimetableViewSet(viewsets.ModelViewSet):
	queryset = Timetable.objects.all()
	serializer_class = TimetableSerializer
	permission_classes = (IsOwner,)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class AttendanceViewSet(viewsets.ModelViewSet):
	queryset = Attendance.objects.all()
	serializer_class = AttendanceSerializer
	permission_classes = (IsOwner,)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

