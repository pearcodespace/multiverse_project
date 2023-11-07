"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hello_world.core import views as core_views 
urlpatterns = [
    path("", core_views.index),
    path('admin/', admin.site.urls),
    path("app_general/", (core_views.app_general), name="home"),
    path("app_general/docs/", (core_views.app_general_docs), name="docs"),
    path("app_reports/", (core_views.app_reports), name="reports"),
    path("app_reports/<int:report_id>/", (core_views.app_reports_report), name="report"),
    path("app_textsentiment/", (core_views.app_textsentiment), name="text_sentiment"),
    path("_reload_/", include("django_browser_reload.urls")),
    path("import/csv", core_views.import_data_csv),
    path("external_api", core_views.call_external_api),
    path("visualize", core_views.linear_regression)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
