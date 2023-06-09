from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView	

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("",TemplateView.as_view(template_name="index.html"), name="home"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)