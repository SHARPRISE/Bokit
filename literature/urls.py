from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.texts, name='literature'),
    url(r'^(?P<slug>[\w\-]+)/$', views.text),
]
