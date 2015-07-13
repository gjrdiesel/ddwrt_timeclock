from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<employee_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<employee_id>[0-9]+)/time/$', views.time, name='time'),
	url(r'^stateupdate/$', views.stateupdate, name='stateupdate'),
]
