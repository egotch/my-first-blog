from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.post_list, name='post_list'),
]

#Add in the static fields for CSS and other things
urlpatterns += staticfiles_urlpatterns()