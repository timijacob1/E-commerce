"""classproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from classproject.adminapp import views as admin_view
from django.views.generic import TemplateView
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_view.index_page, name="homepage"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="About"),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
    path('shop/', TemplateView.as_view(template_name="shop.html"), name="shop"),
    path('shop-single/', TemplateView.as_view(template_name="shop-single.html"), name="shop-single"),
    url(r'^accounts/', include ('django.contrib.auth.urls')),
    url(r'^accounts/signup/ $', admin_view.SignUpView.as_view(), name = "signup"),
]
