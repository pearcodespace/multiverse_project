from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_sentiment, name='text_sentiment')
]