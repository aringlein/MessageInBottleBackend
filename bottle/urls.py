from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^(?P<message_id>[0-9]+)/$', views.info, name='info'),
	url(r'^update/$', views.update, name='update'),
	url(r'^new/$', views.new, name='new'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
]