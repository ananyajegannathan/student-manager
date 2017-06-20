from django.conf.urls import url, include
from reminder import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
# router.register(r'users', views.UserViewSet)
router.register(r'lists', views.ListViewSet, base_name='list')
router.register(r'items', views.ItemViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'timetable', views.TimetableViewSet)
router.register(r'attendance', views.AttendanceViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
	# url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^register/$', views.UserCreate.as_view(), name='user-create'),
	url(r'^api-token-auth/', obtain_jwt_token),
]