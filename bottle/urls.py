from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<message_id>[0-9]+)/$', views.info, name='info'),
    # ex: /polls/5/results/
]