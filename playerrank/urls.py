from django.urls import path
from django.conf.urls import url
from playerrank import views
urlpatterns = [
    url(r'fraction/$', views.Fraction.as_view()),
]