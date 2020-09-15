# publish_blog/urls.py
from django.urls import path
from publish_blog import views

urlpatterns = [path(r'', views.HomePageView.as_view()), ]