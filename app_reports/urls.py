from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports, name='reports'),
    path('<int:report_id>', views.report, name='report'),
]