from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts$', views.contact, name='contact'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^mission$', views.mission, name='mission'),
]
