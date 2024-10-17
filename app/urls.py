
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('prediction',views.prediction,name='prediction')
]