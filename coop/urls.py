from django.urls import include, path
from . import views
from coop.views import AccoutDetailView
import  django.contrib.auth.urls
urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='register'),
    path('save/',views.save, name='save'),
    path('deposit/',views.deposit,name='deposit'),
    path('pay/',views.pay,name='pay'),
    path('member/<int:pk>/',AccoutDetailView.as_view(),name='member-details'),
    path('validate/',views.validate, name='validate'),
    path('query/',views.query,name='query'),
    #USER AUTHENTICATION AND ACCOUNT
    path('accounts/', include('django.contrib.auth.urls')),
]