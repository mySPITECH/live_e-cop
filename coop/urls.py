from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='register'),
    path('save/',views.save_user, name='save'),
]